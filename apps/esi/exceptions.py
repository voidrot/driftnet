import dataclasses

from aiopenapi3.errors import HTTPClientError as BaseHTTPClientError
from aiopenapi3.errors import HTTPServerError as BaseHTTPServerError


class ESIErrorLimitException(Exception):  # noqa: N818
    """ESI Global Error Limit Exceeded
    https://developers.eveonline.com/docs/services/esi/best-practices/#error-limit
    """

    def __init__(self, reset=None, *args, **kwargs) -> None:
        self.reset = reset
        msg = kwargs.get('message') or (
            f'ESI Error limited. Reset in {reset} seconds.'
            if reset
            else 'ESI Error limited.'
        )
        super().__init__(msg, *args)


@dataclasses.dataclass(repr=False)
class HTTPNotModified(Exception):  # noqa: N818
    """
    Exception representing an HTTP 304 Not Modified response.

    Used to indicate that the requested resource has not changed since the last request.
    Contains the HTTP status code and response headers.
    """

    status_code: int
    headers: dict[str, str]

    def __str__(self):
        return f"""<{self.__class__.__name__} {self.status_code} {self.headers}>"""


@dataclasses.dataclass(repr=False)
class HTTPClientError(BaseHTTPClientError):
    """
    Exception representing an HTTP 4xx client error response.

    Inherits from aiopenapi3.errors.HTTPClientError.
    Used to indicate that the client made a request that resulted in a 4xx error code.
    """


@dataclasses.dataclass(repr=False)
class HTTPServerError(BaseHTTPServerError):
    """
    Exception representing an HTTP 5xx server error response.

    Inherits from aiopenapi3.errors.HTTPServerError.
    Used to indicate that the server encountered an error or is otherwise incapable of performing the request.
    """


class ESIException(Exception):  # noqa: N818
    """
    Base exception for all ESI-related errors.

    All custom ESI exceptions should inherit from this class to allow
    unified exception handling for ESI errors throughout the application.
    """


class TokenError(ESIException):
    """
    Base exception for token-related errors in ESI authentication.

    All token exceptions should inherit from this class to allow unified handling
    of authentication and authorization issues related to ESI tokens.
    """


class TokenInvalidError(TokenError):
    """
    Exception raised when an ESI authentication token is invalid.

    This error indicates that the provided token is not recognized or has been revoked,
    and cannot be used for authentication or API requests.
    """


class TokenExpiredError(TokenError):
    """
    Exception raised when an ESI authentication token has expired.

    Indicates that the token is no longer valid due to expiration and cannot be refreshed.
    Typically requires the user to re-authenticate to obtain a new token.
    """


class TokenNotRefreshableError(TokenError):
    """
    Exception raised when an ESI authentication token cannot be refreshed.

    Indicates that the token is not eligible for refresh, possibly due to missing refresh privileges,
    token type restrictions, or other ESI-specific constraints. Requires user re-authentication.
    """
