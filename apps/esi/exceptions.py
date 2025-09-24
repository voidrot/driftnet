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
