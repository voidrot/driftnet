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
