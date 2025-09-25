import base64
import datetime
import logging
from typing import Any
from typing import ClassVar

import httpx
from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.esi import app_settings
from apps.esi.exceptions import TokenError
from apps.esi.exceptions import TokenExpiredError
from apps.esi.exceptions import TokenNotRefreshableError
from apps.esi.managers import TokenManager
from apps.esi.managers import TokenQuerySet

logger = logging.getLogger(__name__)


class Scope(models.Model):
    """A scope defines the access permissions for an ESI token.

    Attributes:
        name (str): The name of the scope.
        description (str): A brief description of what the scope allows.
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Scope'
        verbose_name_plural = 'Scopes'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Token(models.Model):
    """An ESI token representing a user's authentication and authorization.

    Attributes:
        access_token (str): The access token string.
        refresh_token (str): The refresh token string.
        expires_at (datetime): The expiration time of the access token.
        character_id (int): The ID of the character associated with the token.
        character_name (str): The name of the character associated with the token.
        scopes (ManyToMany[Scope]): The scopes associated with this token.
        created_at (datetime): The timestamp when the token was created.
        updated_at (datetime): The timestamp when the token was last updated.
    """

    TOKEN_TYPE_CHARACTER = 'character'  # noqa: S105
    TOKEN_TYPE_CORPORATION = 'corporation'  # noqa: S105
    TOKEN_TYPE_CHOICES = [
        (TOKEN_TYPE_CHARACTER, 'Character'),
        (TOKEN_TYPE_CORPORATION, 'Corporation'),
    ]

    character_id = models.BigIntegerField(db_index=True)
    character_name = models.CharField(max_length=100, db_index=True)
    token_type = models.CharField(
        max_length=50,
        choices=TOKEN_TYPE_CHOICES,
        default=TOKEN_TYPE_CHARACTER,
        db_index=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=255, editable=False)
    refresh_token = models.CharField(max_length=255, editable=False)
    character_owner_hash = models.CharField(max_length=255, db_index=True)
    scopes = models.ManyToManyField(Scope)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ['-created']

    objects: ClassVar[TokenManager] = TokenManager.from_queryset(TokenQuerySet)()

    def __str__(self) -> str:
        try:
            scopes = sorted(s.name for s in self.scopes.all())
        except ValueError:
            scopes = []
        return f'{self.character_name} - {", ".join(scopes)}'

    @property
    def can_refresh(self) -> bool:
        """Indicates if the token can be refreshed.

        Returns:
            bool: True if the token has a non-null refresh_token, False otherwise.
        """
        return bool(self.refresh_token)

    @property
    def expires_at(self) -> datetime.datetime:
        """Calculates the expiration time of the access token.

        Returns:
            datetime: The expiration time of the access token.
        """
        return self.created + datetime.timedelta(
            seconds=settings.ESI_TOKEN_VALID_DURATION
        )

    @property
    def is_expired(self) -> bool:
        """Indicates if the access token is expired.

        Returns:
            bool: True if the current time is past the expiration time, False otherwise.
        """
        return self.expires_at < timezone.now()

    def valid_access_token(self) -> str:
        """Returns a valid access token, refreshing it if necessary.

        If the token is expired and can be refreshed, attempts to refresh it.
        If refreshing fails, raises an exception.

        Returns:
            str: A valid access token.
        """
        if self.is_expired:
            if self.can_refresh:
                self.refresh()
            else:
                raise TokenExpiredError
        return self.access_token

    def refresh(self) -> None:
        """
        Refreshes the access token using the refresh token.

        This method attempts to obtain a new access token from the ESI OAuth endpoint
        using the current refresh token. If the token cannot be refreshed (e.g., missing
        refresh token, owner hash mismatch, or HTTP 4xx error), it raises a TokenNotRefreshableError.

        Raises:
            TokenNotRefreshableError: If the token cannot be refreshed due to missing refresh token,
                owner hash mismatch, or a 4xx error from the OAuth endpoint.
        """
        if not self.can_refresh:
            msg = 'Token cannot be refreshed.'
            raise TokenNotRefreshableError(msg)

        auth = base64.b64encode(app_settings.ESI_BASIC_AUTH_STR.encode('utf-8')).decode(
            'utf-8'
        )

        response = httpx.post(
            app_settings.ESI_OAUTH_URL + '/token',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {auth}',
            },
            data={
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
            },
        )
        if response.status_code in {400, 401}:
            msg = 'Token refresh failed with 4xx error.'
            raise TokenNotRefreshableError(msg)

        token_data = response.json()

        decoded_token = Token.get_token_data(token_data.get('access_token'))

        logger.debug('Token refresh response: %s', decoded_token)

        if token_data is not None and decoded_token is not None:
            if self.character_owner_hash != decoded_token.get('owner'):
                logger.warning(
                    'Owner hash mismatch for token %s: %s != %s',
                    self.pk,
                    self.character_owner_hash,
                    decoded_token.get('owner'),
                )
                # TODO: Create a way to notify the user of the issue
                raise TokenNotRefreshableError

        self.access_token = token_data['access_token']
        self.refresh_token = token_data['refresh_token']
        self.created = timezone.now()
        self.save()

    def refresh_or_delete(self) -> None:
        """
        Attempts to refresh the token; deletes it if refresh fails.

        This method tries to refresh the access token. If a TokenError occurs
        (indicating the token cannot be refreshed), the token is deleted from the database.
        Otherwise, logs a successful refresh.

        This helps maintain valid tokens and automatically cleans up expired or invalid ones.
        """
        try:
            self.refresh()
        except TokenError:
            logger.info(
                'Deleting token for character (ID: %s) %s',
                self.character_id,
                self.character_name,
            )
            self.delete()
        else:
            logger.info(
                'Refreshed token for character (ID: %s) %s',
                self.character_id,
                self.character_name,
            )

    @classmethod
    def get_token_data(cls, access_token: str) -> dict[str, Any] | None:
        """
        Validates and decodes an ESI access token.

        Args:
            access_token (str): The access token to validate and decode.

        Returns:
            dict[str, Any] | None: Decoded token data if valid, otherwise None.
        """
        return TokenManager.validate_access_token(access_token)

    @classmethod
    def get_token(cls, character_id: int, scopes: list) -> 'Token':
        """
        Retrieves a Token for the given character ID with the required scopes.

        Args:
            character_id (int): The ID of the character for which to retrieve the token.
            scopes (list): A list of scope names that the token must include.

        Returns:
            Token: The token object matching the character ID and required scopes.

        Raises:
            TokenError: If no token is found for the character with the required scopes.
        """
        token = (
            Token.objects.filter(character_id=character_id)
            .require_scopes(scopes)
            .first()
        )
        if not token:
            msg = 'No token found for character with required scopes'
            raise TokenError(msg)
        return token


class CallbackRedirect(models.Model):
    """Stores redirect information for ESI OAuth callback flows.

    Used to associate a session and state with a redirect URL and optionally a token,
    enabling secure and traceable OAuth authentication flows.

    Attributes:
        created (datetime): Timestamp when the redirect was created.
        state (str): The OAuth state parameter for CSRF protection.
        session_key (str): Unique session key for the redirect.
        url (str): The URL to redirect to after authentication.
        token (ForeignKey[Token], optional): The associated ESI token, if available.
    """

    created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=128)
    session_key = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.session_key}: {self.url}'
