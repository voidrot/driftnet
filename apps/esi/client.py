import logging
import warnings
from datetime import datetime
from hashlib import md5
from typing import Any

from aiopenapi3 import OpenAPI
from aiopenapi3._types import ResponseDataType
from aiopenapi3._types import ResponseHeadersType
from aiopenapi3.request import OperationIndex
from aiopenapi3.request import RequestBase
from django.core.cache import cache
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

from apps.esi.exceptions import ESIErrorLimitExceptionError
from apps.esi.stubs import ESIClientStub

from .app_settings import ESI_APP_UA_EMAIL
from .app_settings import ESI_APP_UA_NAME
from .app_settings import ESI_APP_UA_URL
from .app_settings import ESI_APP_UA_VERSION
from .app_settings import ESI_CLIENT_CONNECT_TIMEOUT
from .app_settings import ESI_CLIENT_POOL_TIMEOUT
from .app_settings import ESI_CLIENT_READ_TIMEOUT
from .app_settings import ESI_CLIENT_TENANT
from .app_settings import ESI_CLIENT_WRITE_TIMEOUT
from .app_settings import ESI_COMPATIBILITY_DATE
from .app_settings import ESI_OPENAPI_URL
from .models import Token

logger = logging.getLogger(__name__)


def _build_user_agent() -> str:
    """
    Build a User-Agent string for ESI requests.
    """
    return (
        f'{ESI_APP_UA_NAME}/{ESI_APP_UA_VERSION} '
        f'({ESI_APP_UA_EMAIL}{f"; +{ESI_APP_UA_URL})" if ESI_APP_UA_URL else ")"} '
    )


def _time_to_expire(expires_header: str) -> int:
    """
    Calculate cache TTL from an HTTP Expires header.
    """
    try:
        expires = datetime.strptime(expires_header, '%a, %d %b %Y %H:%M:%S %Z')
        return max(int((expires - datetime.utcnow()).total_seconds()), 0)
    except ValueError:
        return 0


def _retry_exceptions(exc: BaseException) -> bool:
    """
    Determine if a request should be retried based on the exception raised.
    """
    if isinstance(exc, ESIErrorLimitException):
        return False
    if isinstance(exc, RequestError):
        return True
    if (  # noqa: SIM103
        isinstance(exc, HTTPStatusError)
        and getattr(exc.response, 'status_code', None) in {502, 503, 504}
    ):
        return True
    # TODO: Add more conditions as needed
    return False


def _request_retry() -> Retrying:
    """
    Configure a Retrying object for request retries.
    """
    return Retrying(
        retry=retry_if_exception(_retry_exceptions),
        wait=wait_combine(
            wait_exponential(multiplier=1, min=4, max=10),
        ),
        stop=stop_after_attempt(3),
        reraise=True,
    )


def _load_openapi_client() -> OpenAPI:
    """
    Load the OpenAPI specification and create an instance of OpenAPI client.
    """
    headers = {
        'User-Agent': _build_user_agent(),
        'X-Tenant': ESI_CLIENT_TENANT,
        'X-Compatibility-Date': ESI_COMPATIBILITY_DATE,
    }

    def session_factory(**kwargs):
        kwargs.pop('headers', None)
        return Client(
            headers=headers,
            timeout=Timeout(
                connect=ESI_CLIENT_CONNECT_TIMEOUT,
                read=ESI_CLIENT_READ_TIMEOUT,
                write=ESI_CLIENT_WRITE_TIMEOUT,
                pool=ESI_CLIENT_POOL_TIMEOUT,
            ),
            http2=True,
            **kwargs,
        )

    return OpenAPI.load_sync(
        url=ESI_OPENAPI_URL,
        session_factory=session_factory,
        use_operation_tags=True,
        plugins=[],
    )


def _client_factory(**kwargs):
    """
    Factory function to create an ESI API client.
    """
    return _load_openapi_client()


class BaseESIClientOperation:
    def __init__(self, operation, api) -> None:
        self.method, self.url, self.operation, self.extra = operation
        self.api: OpenAPI = api
        self.token: Token | None = None
        self._args = []
        self._kwargs = {}

    def __call__(self, *args, **kwargs) -> 'BaseESIClientOperation':
        self._args = args
        self._kwargs = kwargs
        return self

    def _reverse_normalize_params(self, params: dict[str, Any]) -> dict[str, Any]:
        """
        Reverse the normalization of parameters to match the original operation signature.
        """
        # This is a placeholder implementation. The actual implementation would depend
        # on how parameters were normalized in the aiopenapi3 library.
        try:
            spec_param_names = [
                p.name for p in getattr(self.operation, 'parameters', [])
            ]
        except Exception:
            spec_param_names = []

        spec_param_set = set(spec_param_names)
        spec_param_map_ci = {name.lower(): name for name in spec_param_names}

        normalized: dict[str, Any] = {}
        for k, v in params.items():
            # Check for exact match
            if k in spec_param_set:
                normalized[k] = v
                continue

            # Check for hyphen variant
            k_dash = k.replace('_', '-')
            if k_dash in spec_param_set:
                normalized[k_dash] = v
                continue

            # Check for case-insensitive match
            k_lower = k.lower()
            if k_lower in spec_param_map_ci:
                k_dash_lower = k_dash.lower()
                normalized[spec_param_map_ci[k_dash_lower]] = v
                continue

            # Unknown in spec, let aiopenapi3 validate
            normalized[k] = v
        return normalized

    def _cache_key(self) -> str:
        """
        Generate a cache key based on the operation and its parameters.
        """
        data = (self.method + self.url + str(self._args) + str(self._kwargs)).encode(
            'utf-8'
        )
        hash_str = md5(data).hexdigest()  # noqa: S324
        return f'esi:{hash_str}'

    def _get_cache(
        self, cache_key: str
    ) -> tuple[ResponseHeadersType | None, Any, Response | None]:
        """
        Retrieve a cached response if available and validate its freshness.
        """
        try:
            cached_response = cache.get(f'{cache_key}:data')
        except Exception as e:
            logger.error(
                f'Error retrieving cache for key {cache_key}:data : {e}', exc_info=True
            )
            return None, None, None

        if cached_response:
            logger.debug(f'Cache hit for key {cache_key}')
            headers, data = self.parse_cached_request(cached_response)

            expires = _time_to_expire(str(headers.get('Expires')))
            if expires <= 0:
                logger.debug(
                    'Cache expired by %d for key %s, forcing expiration',
                    expires,
                    cache_key,
                )
                cache.delete(cache_key)
                return None, None, None
            return headers, data, cached_response
        return None, None, None

    def _store_cache(self, cache_key: str, response: Response) -> None:
        """
        Store a response in the cache with an ETag and appropriate TTL.
        """
        if 'ETag' in response.headers:
            cache.set(f'{cache_key}:etag', response.headers['ETag'])

        expires = response.headers.get('Expires')
        ttl = _time_to_expire(expires) if expires else 0
        if ttl > 0:
            try:
                cache.set(f'{cache_key}:data', response, ttl)
                logger.debug(
                    f'Stored response in cache with key {cache_key} for {ttl}s'
                )
            except Exception:
                logger.exception(f'Error storing cache for key {cache_key}')

    def _extract_token_param(self) -> Token | None:
        """
        Extract the token from parameters or use the client wide token if it has been set.
        """
        _token = self._kwargs.pop('token', None)
        if _token and not getattr(self.operation, 'security', None):
            msg = 'Token provided on public endpoint'
            raise ValueError(msg)
        return self.token or _token

    def _has_pages(self) -> bool:
        """
        Determine if the operation supports pagination.
        """
        return any(p.name == 'page' for p in self.operation.parameters)

    def _has_cursor(self) -> bool:
        """
        Determine if the operation supports cursor-based pagination.
        """
        return any(p.name in {'before', 'after'} for p in self.operation.parameters)

    def _validate_token_scopes(self, token: Token) -> None:
        """
        Validate that the provided token has the required scopes for this operation.
        """
        token_scopes = set(token.scopes.all().values_list('name', flat=True))
        try:
            required_scopes = set(
                getattr(getattr(self.operation, 'security', [])[0], 'root', {}).get(
                    'OAuth2', []
                )
            )
        except KeyError:
            required_scopes = []
        missing_scopes = [x for x in required_scopes if x not in token_scopes]
        if len(missing_scopes) > 0:
            msg = f'Token missing required scopes: {", ".join(missing_scopes)}'
            raise ValueError(
                msg
            )  # TODO: Should we add a custom exception for missing scopes

    def parse_cached_request(
        self, cached_response: Response
    ) -> tuple[ResponseHeadersType, ResponseDataType]:
        """
        Parse a cached Response object to extract headers and data.
        """
        req = self.api.createRequest(
            f'{self.operation.tags[0]}.{self.operation.operationId}'
        )
        return req._process_request(cached_response)


class ESIClientOperation(BaseESIClientOperation):
    def _make_request(
        self, parameters: dict[str, Any], etag: str | None = None
    ) -> RequestBase.Response:
        reset = cache.get('esi_rate_limit:error_limit_reset')
        if reset is not None:
            # Hard stop if there is still an active error limit
            raise ESIErrorLimitExceptionError(reset=reset)

        retry = _request_retry()

        def __func():
            req = self.api.createRequest(
                f'{self.operation.tags[0]}.{self.operation.operationId}'
            )
            if self.token:
                self.api.authenticate(OAuth2=True)
                if isinstance(self.token, str):
                    req.req.headers['Authorization'] = f'Bearer {self.token}'
                    warnings.warn(
                        'Passing an Access Token string directly is deprecated.'
                        'Doing so will Skip Validation of Scopes'
                        'Please use a Token object instead.',
                        DeprecationWarning,
                        stacklevel=2,
                    )
                else:
                    self._validate_token_scopes(self.token)
                    req.req.headers['Authorization'] = (
                        f'Bearer {self.token.valid_access_token()}'
                    )
            if etag:
                req.req.headers['If-None-Match'] = etag
            return req.request(parameters=self._reverse_normalize_params(parameters))

        return retry(__func)

    def result(self):
        raise NotImplementedError

    def result_localized(self):
        raise NotImplementedError

    def results(self):
        raise NotImplementedError

    def results_localized(self):
        raise NotImplementedError

    def required_scopes(self) -> list[str]:
        """
        Return a list of scopes required for this operation.
        """
        try:
            if not getattr(self.operation, 'security', None):
                return []  # No required scopes for this operation
            return list(
                getattr(getattr(self.operation, 'security', [])[0], 'root', {}).get(
                    'OAuth2', []
                )
            )
        except (IndexError, KeyError):
            return []


class ESITag:
    """
    API Tag wrapper to provide access to operations under a specific tag.
    """

    def __init__(self, operation, api) -> None:
        self._op_index = operation._oi
        self._operations = operation._operations
        self.api = api

    def __getattr__(self, name: str) -> ESIClientOperation:
        if name not in self._operations:
            msg = (
                f"Operation '{name}' not found in tag. ",
                f'Available operations: {", ".join(sorted(self._operations.keys()))}',
            )
            raise AttributeError(msg)
        return ESIClientOperation(self._operations[name], self.api)


class ESIClient(ESIClientStub):
    def __init__(self, api: OpenAPI) -> None:
        self.api: OpenAPI = api
        self._tags = set(api._operationindex._tags.keys())

    def __getattr__(self, tag: str) -> ESITag | OperationIndex:
        # underscore returns the raw aiopenapi3 client
        if tag == '_':
            return self.api._operationindex

        if tag in set(self.api._operationindex._tags.keys()):
            return ESITag(self.api._operationindex._tags[tag], self.api)

        msg = (
            f"Tag '{tag}' not found. ",
            f'Available tags: {", ".join(sorted(self._tags))}',
        )
        raise AttributeError(msg)


class ESIClientProvider:
    """
    Class to provide a single point of access to the ESI API client.
    """

    def __init__(self, **kwargs) -> None:
        self._kwargs = kwargs

    @property
    def client(self) -> ESIClient:
        if self._client is None:
            api = _client_factory(**self._kwargs)
            self._client = ESIClient(api)
        return self._client

    def __str__(self) -> str:
        return 'ESIClientProvider'
