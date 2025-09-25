import logging
from hashlib import blake2b
from typing import Any

from aiopenapi3 import HTTPError
from aiopenapi3 import OpenAPI
from aiopenapi3._types import ResponseDataType
from aiopenapi3._types import ResponseHeadersType
from aiopenapi3.errors import HTTPClientError as BaseHTTPClientError
from aiopenapi3.errors import HTTPServerError as BaseHTTPServerError
from aiopenapi3.request import OperationIndex
from aiopenapi3.request import RequestBase
from django.core.cache import CacheHandler
from django.core.cache import caches
from httpx import Client
from httpx import HTTPStatusError
from httpx import RequestError
from httpx import Response
from httpx import Timeout
from tenacity import Retrying
from tenacity import retry_if_exception
from tenacity import stop_after_attempt
from tenacity import wait_combine
from tenacity import wait_exponential

from apps.esi import app_settings
from apps.esi.client_stubs import ESIClientStub
from apps.esi.exceptions import ESIErrorLimitException
from apps.esi.exceptions import HTTPClientError
from apps.esi.exceptions import HTTPNotModified
from apps.esi.models import Token
from apps.esi.plugins import Add304ContentType
from apps.esi.plugins import PatchCompatibilityDatePlugin
from apps.esi.plugins import Trim204ContentType

logger = logging.getLogger(__name__)

DEFAULT_EXPIRY = 60 * 60 * 24 * 5  # 5 days


def _get_user_agent() -> str:
    """
    Constructs and returns the User-Agent string for ESI requests.

    The User-Agent includes the application name, version, contact email, and optionally the application URL.
    This helps ESI API maintainers identify the source of requests and contact the responsible party if needed.
    """
    email = app_settings.ESI_CONTACT_EMAIL
    url = app_settings.ESI_APP_URL
    name = app_settings.ESI_APP_NAME
    version = app_settings.ESI_APP_VERSION
    return f'{name}/{version} {email}{f" (+{url})" if url else ""}'


def _httpx_exception_retries(exception: Exception) -> bool:
    """
    Determines whether the given exception should trigger a retry for ESI requests.

    Retries are triggered for network-related errors (RequestError) and HTTP errors with status codes 502, 503, or 504.
    This helps improve reliability when facing transient issues or temporary service outages.
    """

    # TODO: Add custom ESI exceptions here as needed
    if isinstance(exception, ESIErrorLimitException):
        return False
    if isinstance(exception, RequestError):
        return True
    if (  # noqa: SIM103
        isinstance(exception, HTTPStatusError)
        and getattr(exception.response, 'status_code', None) in {502, 503, 504}
    ):
        return True
    return False


def _request_retry() -> Retrying:
    """
    Configure and return a Retrying object for ESI requests.

    Retries on network-related exceptions and HTTP 502/503/504 errors,
    using exponential backoff (min 1s, max 10s), up to 3 attempts.
    Raises the last exception if all retries fail.
    """
    return Retrying(
        retry=retry_if_exception(_httpx_exception_retries),
        wait=wait_combine(
            wait_exponential(multiplier=1, min=1, max=10),
        ),
        stop=stop_after_attempt(3),
        reraise=True,
    )


def _load_openapi_plugins():
    """
    Load and return the list of OpenAPI plugins to use with the ESI client.

    This can be extended in the future to add custom plugins for logging, metrics, etc.
    """
    return [PatchCompatibilityDatePlugin(), Trim204ContentType(), Add304ContentType()]


def _load_aiopenapi_client() -> OpenAPI:
    headers = {
        'User-Agent': _get_user_agent(),
        'X-Tenant': app_settings.ESI_CLIENT_TENANT,
        'X-Compatibility-Date': app_settings.ESI_COMPATIBILITY_DATE,
    }

    def session_factory(**kwargs) -> Client:
        kwargs.pop('headers', None)  # Remove any existing headers
        return Client(
            headers=headers,  # replace with our custom headers
            timeout=Timeout(
                connect=app_settings.ESI_CLIENT_CONNECT_TIMEOUT,
                read=app_settings.ESI_CLIENT_READ_TIMEOUT,
                write=app_settings.ESI_CLIENT_WRITE_TIMEOUT,
                pool=app_settings.ESI_CLIENT_POOL_TIMEOUT,
            ),
            http2=True,
            **kwargs,
        )

    return OpenAPI.load_sync(
        url=app_settings.ESI_OPENAPI_URL,
        session_factory=session_factory,
        use_operation_tags=True,
        plugins=_load_openapi_plugins(),
    )


class BaseESIClientOperation:
    def __init__(self, operation, api: OpenAPI) -> None:
        logger.info('operation param is %s', type(operation))
        self._cache: CacheHandler = caches[app_settings.ESI_CACHE_BACKEND_NAME]
        self.api = api
        self.token: Token | None = None
        self._args = []
        self._kwargs = {}
        self.method, self.url, self.operation, self.extra = operation

    def __call__(self, *args, **kwargs) -> 'BaseESIClientOperation':
        self._args = args
        self._kwargs = kwargs
        return self

    def _reverse_normalize_parameters(
        self, parameters: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Converts Python-style snake_case parameter names to the camelCase or dash-case format
        expected by the ESI OpenAPI specification.

        This method attempts to match each parameter name to the specification's parameter names
        using exact, dash, and case-insensitive matching strategies. If no match is found, the
        original parameter name is used. This ensures compatibility between Python code and the
        ESI API's expected parameter naming conventions.

        Args:
            parameters (dict[str, Any]): Dictionary of parameters using Python naming conventions.

        Returns:
            dict[str, Any]: Dictionary of parameters normalized to ESI API specification naming.
        """
        try:
            spec_param_names = [
                p.name for p in getattr(self.operation, 'parameters', [])
            ]
        except Exception:
            spec_param_names = []

        # Build a set for both case-insensitive and exact lookups
        spec_param_set = set(spec_param_names)
        spec_param_map_ci = {n.lower(): n for n in spec_param_names}

        normalized: dict[str, Any] = {}
        for k, v in parameters.items():
            # Exact match first
            if k in spec_param_set:
                normalized[k] = v
                continue

            # Try dash match
            k_dash = k.replace('_', '-')
            if k_dash in spec_param_set:
                normalized[k_dash] = v
                continue

            # Try case insensitive match
            k_lower = k.lower()
            if k_lower in spec_param_map_ci:
                normalized[spec_param_map_ci[k_lower]] = v
                continue

            # Try dash case insensitive match
            k_dash_lower = k_dash.lower()
            if k_dash_lower in spec_param_map_ci:
                normalized[spec_param_map_ci[k_dash_lower]] = v
                continue

            # Passthrough if no match found and let aiopenapi3 lib handle it
            normalized[k] = v

        return normalized

    def _etag_cache_key(self) -> str:
        """
        Returns the cache key used to store the ETag value for this operation.

        The ETag cache key is derived from the operation's cache key and is used to
        efficiently track and validate cached responses for conditional requests.
        """
        return f'{self._cache_key()}:etag'

    def _cache_key(self) -> str:
        """
        Generates a unique cache key for the current ESI client operation.

        The cache key is derived from the HTTP method, URL, positional arguments, and keyword arguments
        (excluding the 'token' parameter). This ensures that cached responses are correctly identified
        based on the operation's input parameters, while ignoring authentication tokens to maximize cache reuse.

        Returns:
            str: A unique cache key string for the operation.
        """
        # Ignore the token for generating the cache key. The token can change but the response will not.
        ignore = ['token']
        new_kwargs = {k: v for k, v in self._kwargs.items() if k not in ignore}
        hash_data = (self.method + self.url + str(self._args) + str(new_kwargs)).encode(
            'utf-8'
        )
        hash_str = blake2b(hash_data, digest_size=24).hexdigest()
        return f'esi:{hash_str}'

    def _get_body_params(self) -> Any | None:
        """
        Retrieves and validates the request body parameter for the ESI operation.

        If a 'body' parameter is present in the keyword arguments, this method checks whether
        the operation's OpenAPI specification defines a request body. If not, it raises a ValueError
        to prevent sending a body to endpoints that do not expect one.

        Returns:
            Any | None: The request body if present and valid, otherwise None.

        Raises:
            ValueError: If a request body is provided but the OpenAPI spec does not define 'requestBody'.
        """
        body = self._kwargs.pop('body', None)
        if body and not getattr(body, 'requestBody', False):
            msg = 'request body send to e3endpoint without requestBody defined in OpenAPI spec'
            raise ValueError(msg)
        return body

    def _get_token_param(self) -> Token | None:
        """
        Retrieves the authentication token parameter for the ESI operation.

        This method pops the 'token' from keyword arguments and validates whether it is appropriate
        to send to the endpoint (i.e., only to endpoints that require security). If the token is present
        but the endpoint does not expect authentication, a ValueError is raised.

        Returns:
            Token | None: The token to use for authentication, or None if not required.

        Raises:
            ValueError: If a token is provided for a public endpoint that does not require authentication.
        """
        token = self._kwargs.pop('token', None)
        if token and not getattr(token, 'security', False):
            msg = 'Can not send token to public endpoints'
            raise ValueError(msg)
        return self.token or token

    def _has_pages(self) -> bool:
        """
        Determines if the OpenAPI operation supports page-based pagination.

        Checks the operation's parameters for a 'page' parameter, which indicates
        that the endpoint supports pagination via page numbers.

        Returns:
            bool: True if a 'page' parameter is present, False otherwise.
        """
        return any(p.name == 'page' for p in self.operation.parameters)

    def _has_cursor(self) -> bool:
        """
        Determines if the OpenAPI operation supports cursor-based pagination.

        Checks for the presence of 'before' or 'after' parameters in the operation,
        which indicate that the endpoint uses cursor-style pagination instead of page numbers.

        Returns:
            bool: True if cursor-based pagination parameters are present, False otherwise.
        """
        return any(p.name in {'before', 'after'} for p in self.operation.parameters)

    def _get_cache(
        self, cache_key: str, etag: str
    ) -> tuple[ResponseHeadersType | None, Any, Response | None]:
        """
        Retrieves a cached ESI API response based on the provided cache key and ETag.

        If response caching is enabled, attempts to fetch the cached response from the configured cache backend.
        If an ETag is provided and matches the cached response's ETag, the ETag TTL is reset.
        Returns the parsed response headers, data, and the raw cached response object.
        If no cache is found or an error occurs, returns (None, None, None).

        Args:
            cache_key (str): The cache key used to look up the cached response.
            etag (str): The ETag value to validate against the cached response.

        Returns:
            tuple: (ResponseHeadersType | None, Any, Response | None)
                - Response headers if cache is found, else None.
                - Parsed response data if cache is found, else None.
                - Raw cached Response object if cache is found, else None.
        """
        if not app_settings.ESI_CACHE_RESPONSE:
            return None, None, None
        try:
            cache = self._cache.get(cache_key)
        except Exception as e:
            logger.warning('Error getting cache for key %s: %s', cache_key, e)
            return None, None, None

        if cache:
            logger.debug('Cache hit for key %s', cache_key)
            if etag:
                if cache.headers.get('etag') == etag:
                    logger.debug('ETag match for key %s', cache_key)
                    # Reset ETag ttl
                    self._store_etag(
                        etag
                    )  # TODO: move this to the same area we will reset cached data?
            headers, data = self.parse_cached_response(cache)
            return headers, data, cache
        logger.debug('Cache miss for key %s', cache_key)
        return None, None, None

    def _store_etag(self, etag: str | dict) -> None:
        """
        Stores the ETag value in the cache for the current operation.

        This method is used to persist the ETag associated with a cached response, enabling efficient
        conditional requests and cache validation. If the provided etag is a dictionary, it extracts
        the 'etag' value. The ETag is stored using a unique cache key and a default expiry period.

        Args:
            etag (str | dict): The ETag value to store, or a dictionary containing an 'etag' key.

        Returns:
            None
        """
        if isinstance(etag, dict):
            etag = etag.get('etag')
        self._cache.set(self._etag_cache_key(), etag, DEFAULT_EXPIRY)

    def _remove_etag(self) -> None:
        """
        Removes the cached ETag value for this operation.

        This method deletes the ETag entry from the cache, ensuring that subsequent requests
        will not use a stale ETag for conditional requests. This is useful when the cached ETag
        is no longer valid or needs to be refreshed.
        """
        try:
            self._cache.delete(self._etag_cache_key())
        except Exception as e:
            logger.error('Error deleting etag cache: %s', e, exc_info=True)  # noqa: G201

    def _store_response(self, cache_key: str, response: Response) -> None:
        """
        Stores the given HTTP response in the cache for the current ESI client operation.

        This method caches the response using a unique cache key derived from the operation's parameters,
        enabling efficient reuse of API responses and reducing redundant network requests.
        Caching is only performed if ESI response caching is enabled in the application settings.

        Args:
            response (Response): The HTTP response object to cache.

        Returns:
            None
        """
        if not app_settings.ESI_CACHE_RESPONSE:
            return
        try:
            self._cache.set(cache_key, response, DEFAULT_EXPIRY)
        except Exception as e:
            logger.error(  # noqa: G201
                'Error setting response cache for key %s: %s',
                cache_key,
                e,
                exc_info=True,
            )

    def _clear_cache(self) -> None:
        """
        Removes the cached response for the current ESI client operation.

        This method deletes the cached response entry from the cache backend, ensuring that subsequent requests
        will not use stale cached data. Useful when the cached response is outdated or needs to be refreshed.
        """
        try:
            self._cache.delete(self._cache_key())
        except Exception as e:
            logger.error('Error deleting response cache: %s', e, exc_info=True)  # noqa: G201

    def _validate_token_scopes(self, token: Token) -> None:
        """
        Validates that the provided token contains all required OAuth2 scopes for the current ESI operation.

        This method compares the token's scopes against the scopes required by the operation's OpenAPI security definition.
        If any required scopes are missing from the token, a ValueError is raised listing the missing scopes.

        Args:
            token (Token): The authentication token to validate.

        Raises:
            ValueError: If the token is missing one or more required scopes for the operation.
        """
        token_scopes = set(token.scopes.all().values_list('name', flat=True))

        try:
            scopes_required = set(
                getattr(getattr(self.operation, 'security', [])[0], 'root', {}).get(
                    'OAuth2', []
                )
            )
            logger.debug(
                'Token scopes: %s, required scopes: %s', token_scopes, scopes_required
            )
        except KeyError:
            scopes_required = []
        scopes_missing = [s for s in scopes_required if s not in token_scopes]
        if len(scopes_missing) > 0:
            msg = f'Token is missing required scopes: {", ".join(scopes_missing)}'
            raise ValueError(msg)

    def parse_cached_response(
        self, cached_response: Response
    ) -> tuple[ResponseHeadersType, ResponseDataType]:
        """
        Parses a cached HTTP response object into structured response headers and data.

        This method uses the OpenAPI client to reconstruct the expected response format
        from a cached Response object, enabling consistent handling of cached and live responses.

        Args:
            cached_response (Response): The cached HTTP response object.

        Returns:
            tuple[ResponseHeadersType, ResponseDataType]: A tuple containing the parsed response headers and data.
        """
        req = self.api.createRequest(
            f'{self.operation.tags[0]}.{self.operation.operationId}'
        )
        return req._process_request(cached_response)


class ESIClientOperation(BaseESIClientOperation):
    def _make_request(
        self, parameters: dict[str, Any], etag: str | None = None
    ) -> RequestBase.Response:
        """
        Executes an ESI API request with retry logic and optional ETag support.

        This method checks for error limit resets, applies retry logic for transient errors,
        and constructs the request using the OpenAPI client. If a token is present, it authenticates
        the request and validates required scopes. If an ETag is provided, it is sent for conditional requests.

        Args:
            parameters (dict[str, Any]): The parameters for the API request.
            etag (str | None): Optional ETag value for conditional requests.

        Returns:
            RequestBase.Response: The response object from the API request.

        Raises:
            ESIErrorLimitException: If the error limit reset is active.
            ValueError: If token scopes are invalid or authentication fails.
        """
        reset = self._cache.get('esi_error_limit_reset')
        if reset is not None:
            # If we are error limited, do not make the request
            raise ESIErrorLimitException(reset=reset)
        retry = _request_retry()

        def __func():
            req = self.api.createRequest(
                f'{self.operation.tags[0]}.{self.operation.operationId}'
            )
            if self.token:
                self.api.authenticate(OAuth2=True)
                self._validate_token_scopes(self.token)
                req.req.headers['Authorization'] = f'Bearer {self.token}'
            if etag:
                req.req.headers['If-None-Match'] = etag
            return req.request(
                data=self.body,
                parameters=self._reverse_normalize_parameters(parameters),
            )

        return retry(__func)

    def result(
        self,
        use_etag: bool = True,
        return_response: bool = False,
        force_refresh: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> tuple[Any, Response] | Any:
        """
        Executes the ESI API operation and returns the result, optionally using ETag and cache.

        Args:
            use_etag (bool): Whether to use ETag for conditional requests and caching.
            return_response (bool): If True, returns a tuple of (data, response); otherwise, returns only data.
            force_refresh (bool): If True, clears cache and ETag before making the request.
            use_cache (bool): If True, attempts to use cached responses.
            **extra: Additional keyword arguments passed to the operation.

        Returns:
            tuple[Any, Response] | Any: The parsed response data, or a tuple of (data, response) if return_response is True.

        Raises:
            HTTPNotModified: If the response status is 304 and no cached response is available.
            HTTPClientError: For client-side HTTP errors.
            HTTPError: For server-side HTTP errors.
            ESIErrorLimitException: If the error limit reset is active.
        """
        self.token = self._get_token_param()
        self.body = self._get_body_params()
        parameters = self._kwargs | extra
        cache_key = self._cache_key()
        etag_key = self._etag_cache_key()
        etag = None

        if force_refresh:
            self._clear_cache()
            self._remove_etag()

        if use_etag:
            etag = self._cache.get(etag_key)

        headers, data, response = (
            self._get_cache(cache_key, etag=etag) if use_cache else (None, None, None)
        )

        if not response:
            logger.debug(f'cache disabled or missed {self.url}')
            try:
                headers, _data, response = self._make_request(parameters, etag=etag)
                if response.status_code == 420:  # noqa: PLR2004
                    reset = response.headers.get('X-RateLimit-Reset', None)
                    self._cache.set('esi_error_limit_reset', reset, timeout=reset)
                    raise ESIErrorLimitException(reset=reset)
            except BaseHTTPClientError as e:
                raise HTTPClientError(
                    status_code=e.status_code,
                    headers=e.headers,
                    data=e.data,
                ) from e
            except BaseHTTPServerError as e:
                raise HTTPError(
                    status_code=e.status_code,
                    headers=e.headers,
                    data=e.data,
                ) from e

            if response.status_code == 304:  # noqa: PLR2004
                self._store_etag(response.headers)
                # We dont have a cached response, so we need to make a new request without the etag
                # TODO: Delete etag when missing cache?
                raise HTTPNotModified(
                    status_code=304,
                    headers=headers,
                )
        # Store cache again without including the cached None response from the 304
        self._store_response(cache_key, response)
        # Return the data and response if requested or just the data if not
        return (data, response) if return_response else data

    def results(
        self,
        use_etag: bool = True,
        return_response: bool = False,
        force_refresh: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> tuple[list[Any], Response | Any | None] | list[Any]:
        """
        Executes the ESI API operation and returns all paginated or cursor-based results.

        This method automatically handles pagination (via 'page' parameter) or cursor-based pagination (via 'before'/'after' parameters),
        aggregating results across all pages or cursors. For endpoints without pagination, returns a single result set.

        Args:
            use_etag (bool): Whether to use ETag for conditional requests and caching.
            return_response (bool): If True, returns a tuple of (all_results, last_response); otherwise, returns only all_results.
            force_refresh (bool): If True, clears cache and ETag before making requests.
            use_cache (bool): If True, attempts to use cached responses.
            **extra: Additional keyword arguments passed to the operation.

        Returns:
            tuple[list[Any], Response | Any | None] | list[Any]: A list of all results, or a tuple of (all_results, last_response) if return_response is True.

        Raises:
            HTTPNotModified: If the response status is 304 and no cached response is available.
            HTTPClientError: For client-side HTTP errors.
            HTTPError: For server-side HTTP errors.
            ESIErrorLimitException: If the error limit reset is active.
        """
        all_results: list[Any] = []
        last_response: Response | None = None

        if self._has_pages():
            current_page = 1
            total_pages = 1  # Default to 1 in case header is missing
            while current_page <= total_pages:
                self._kwargs['page'] = current_page
                data, response = self.result(
                    use_etag=use_etag,
                    return_response=True,
                    force_refresh=force_refresh,
                    use_cache=use_cache,
                    **extra,
                )
                last_response = response
                all_results.extend(data if isinstance(data, list) else [data])
                # Update total_pages from the response headers if available
                total_pages = int(response.headers.get('X-Pages', '1'))
                logger.debug(
                    'Fetched page %d of %d, total results so far: %d',
                    current_page,
                    total_pages,
                    len(all_results),
                )
                current_page += 1
        elif self._has_cursor():
            # Untested, only a single endpoint uses this currently
            params = self._kwargs.copy()
            params.update(extra)
            for cursor_param in ('after', 'before'):
                if params.get(cursor_param):
                    break
            else:
                cursor_param = 'after'  # Default to 'after' if none provided
            while True:
                data, response = self.result(
                    use_etag=use_etag,
                    return_response=True,
                    force_refresh=force_refresh,
                    use_cache=use_cache,
                    **params,
                )
                last_response = response
                if not data:
                    break
                all_results.extend(data if isinstance(data, list) else [data])
                cursor_token = {k.lower(): v for k, v in response.headers.items()}.get(
                    cursor_param
                )
                if not cursor_token:
                    break
                params[cursor_param] = cursor_token
        else:
            data, response = self.result(
                use_etag=use_etag,
                return_response=True,
                force_refresh=force_refresh,
                use_cache=use_cache,
                **extra,
            )
            all_results.extend(data if isinstance(data, list) else [data])
            last_response = response

        return (all_results, last_response) if return_response else all_results


class ESITag:
    """
    Represents a tag grouping of ESI API operations.

    Provides dynamic access to operations within a specific tag, allowing attribute-style access to each operation.
    Raises AttributeError if an operation is not found within the tag.
    """

    def __init__(self, operation: OperationIndex.OperationTag, api: OpenAPI) -> None:
        self._oi = operation._oi
        self._operations = operation._operations
        self.api = api

    def __getattr__(self, name: str) -> ESIClientOperation:
        if name not in self._operations:
            msg = (
                f'Operation "{name}" not found in tag "{self._oi}".'
                f'Available operations: {", ".join(sorted(self._operations.keys()))}'
            )
            raise AttributeError(
                msg,
            )
        return ESIClientOperation(self._operations[name], self.api)


class ESIClient(ESIClientStub):
    """
    ESIClient provides dynamic access to ESI API tags and operations.

    This class wraps an OpenAPI client and exposes API tags as attributes, allowing attribute-style access to grouped operations.
    Tags can be accessed using their natural language names or snake_case equivalents. The raw operation index is available via the '_' attribute.
    Raises AttributeError if a requested tag does not exist.

    Example usage:
        client = ESIClient(api)
        market = client.market  # Access the 'market' tag
        operation = market.get_markets_region_orders  # Access an operation within the tag
    """

    def __init__(self, api: OpenAPI) -> None:
        self.api = api
        self._tags = set(api._operationindex._tags.keys())

    def __getattr__(self, tag: str) -> ESITag | OperationIndex:
        # underscore or sad smiley as aiopenapi3 calls it returns the raw api
        if tag == '_':
            return self.api._operationindex

        # Convert snake_case to natural language names
        if '_' in tag:
            tag = tag.replace('_', ' ')

        # Check if the tag exists in the API
        if tag in set(self.api._operationindex._tags.keys()):
            return ESITag(self.api._operationindex._tags[tag], self.api)

        # Tag not found, raise an AttributeError with available tags
        msg = f'Tag "{tag}" not found in ESI API. Available tags: {self._tags}'
        raise AttributeError(msg)

    def purge_cache(self) -> None:
        """
        Purges all cached ESI responses and ETags.

        This method clears the entire cache backend used for storing ESI API responses and ETags.
        Use with caution, as it will remove all cached data, potentially leading to increased
        API requests until the cache is repopulated.
        """
        try:
            from django_redis import get_redis_connection  # noqa: PLC0415

            _client = get_redis_connection(app_settings.ESI_CACHE_BACKEND_NAME)
        except (NotImplementedError, ImportError):
            from django.core.cache import caches  # noqa: PLC0415

            default_cache = caches['default']
            _client = default_cache.get_master_client()

        keys = _client.keys('esi:*')
        if keys:
            deleted = _client.delete(*keys)
        logger.info('Purged %d ESI cache keys', deleted)


class ESIClientProvider:
    """
    Provides a singleton instance of ESIClient for interacting with the ESI API.

    This class manages the lifecycle of the ESIClient, ensuring that only one instance is created and reused.
    It accepts configuration parameters via kwargs, which can be used for client customization.
    Access the client via the `client` property, which lazily initializes the ESIClient if it does not already exist.
    """

    _client: ESIClient | None = None

    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs

    @property
    def client(self) -> ESIClient:
        if self._client is None:
            self._client = ESIClient(_load_aiopenapi_client())
        return self._client

    def __str__(self) -> str:
        return f'ESIClientProvider({self._kwargs})'
