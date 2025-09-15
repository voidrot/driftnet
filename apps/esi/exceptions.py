import dataclasses

from aiopenapi3.errors import HTTPClientError as base_HTTPClientError
from aiopenapi3.errors import HTTPError
from aiopenapi3.errors import HTTPServerError as base_HTTPServerError


class ESIErrorLimitExceptionError(Exception):
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


class ESIBucketLimitExceptionError(Exception):
    """Endpoint (Bucket) Specific Rate Limit Exceeded"""

    def __init__(self, bucket, *args, **kwargs) -> None:
        self.bucket = bucket
        msg = kwargs.get('message') or f'ESI bucket limit reached for {bucket}.'
        super().__init__(msg, *args)


@dataclasses.dataclass(repr=False)
class HTTPNotModified(HTTPError):
    """The HTTP Status is 304"""

    status_code: int
    headers: dict[str, str]

    def __str__(self):
        return f"""<{self.__class__.__name__} {self.status_code} {self.headers}>"""


@dataclasses.dataclass(repr=False)
class HTTPClientError(base_HTTPClientError):
    """response code 4xx"""


@dataclasses.dataclass(repr=False)
class HTTPServerError(base_HTTPServerError):
    """response code 5xx"""


class ESIException(Exception):  # noqa: N818
    """Base ESI Exception"""


class TokenError(ESIException):
    """Base Token Exception"""


class TokenInvalidError(TokenError):
    """The token is invalid."""


class TokenExpiredError(TokenError):
    """The token has expired and can not be refreshed."""


class TokenNotRefreshableError(TokenError):
    """The token can not be refreshed."""
