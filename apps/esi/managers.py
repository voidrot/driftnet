import logging
from datetime import timedelta
from typing import Any

from django.db import models
from django.http import HttpRequest
from django.utils import timezone

from apps.esi import app_settings
from apps.esi.helpers import exchange_code_for_token
from apps.esi.helpers import validate_jwt_token

logger = logging.getLogger(__name__)


def _process_scopes(scopes) -> set[str]:
    """
    Normalize and process ESI scopes input into a set of strings.

    Accepts scopes as None, a space-delimited string, a list containing a single space-delimited string,
    or a list of individual scope strings. Returns a set of scope strings for consistent downstream usage.

    Args:
        scopes: None, str, list[str], or QuerySet representing ESI scopes.

    Returns:
        set[str]: Set of normalized scope strings.
    """
    if scopes is None:
        # support filtering by no scopes with None passed
        scopes = []
    if not isinstance(scopes, models.QuerySet) and len(scopes) == 1:
        # support a single space-delimited string inside a list because :users:
        scopes = scopes[0]
    # support space-delimited string scopes or lists
    if isinstance(scopes, str):
        scopes = set(scopes.split())
    return {str(s) for s in scopes}


class TokenQuerySet(models.QuerySet['Token']):
    def get_expired_tokens(self) -> 'TokenQuerySet':
        """
        Return a queryset of tokens that have expired based on the configured
        ESI token valid duration. This is used to identify tokens that need
        to be refreshed or deleted.

        Returns:
            TokenQuerySet: Queryset of expired Token instances.
        """
        max_age = timezone.now() - timedelta(
            seconds=app_settings.ESI_TOKEN_VALID_DURATION
        )
        return self.filter(created__lte=max_age)

    def bulk_refresh_tokens(self) -> 'TokenQuerySet':
        """
        Refreshes all tokens in the queryset that have a non-null refresh_token.
        For each token, attempts to call its refresh method. If refreshing fails,
        logs the exception and excludes the token from the returned queryset.
        After refreshing, deletes any expired tokens with a non-null refresh_token.

        Returns:
            TokenQuerySet: Queryset of tokens that were successfully refreshed.
        """
        refreshed_pks = []
        for model in self.filter(refresh_token__isnull=False):
            try:
                model.refresh()
                logger.debug(
                    'Refreshed token for character %s (%s)',
                    model.character_name,
                    model.character_id,
                )
                refreshed_pks.append(model.pk)
            except Exception as e:
                logger.exception(
                    'Failed to refresh token for character %s (%s): %s',
                    model.character_name,
                    model.character_id,
                    e,
                )
        self.filter(refresh_token__isnull=False).get_expired_tokens().delete()
        return self.filter(pk__in=refreshed_pks)

    def require_scopes(self, scope_string: str | list[str]) -> 'TokenQuerySet':
        """
        Filter tokens to those that possess all required ESI scopes.

        Accepts a space-delimited string or a list of scope strings, normalizes them,
        and filters the queryset to tokens that have all specified scopes. If any scope
        does not exist, returns an empty queryset. If no scopes are provided, filters
        tokens with no scopes.

        Args:
            scope_string (str | list[str]): Space-delimited string or list of scope names.

        Returns:
            TokenQuerySet: Queryset of tokens matching all required scopes.
        """
        scopes = _process_scopes(scope_string)
        if not scopes:
            return self.filter(scopes__isnull=True)
        from .models import Scope  # Avoid circular import  # noqa: PLC0415

        scope_pks = Scope.objects.filter(name__in=scopes).values_list('pk', flat=True)
        if len(scopes) != len(scope_pks):
            # Some scopes do not exist, so no tokens can match
            return self.none()
        tokens = self.all()
        for pk in scope_pks:
            tokens = tokens.filter(scopes__id=pk)
        return tokens

    def require_scopes_exact(self, scope_string: str | list) -> 'TokenQuerySet':
        """
        Filter tokens to those that possess exactly the specified ESI scopes.

        Accepts a space-delimited string or a list of scope strings, normalizes them,
        and filters the queryset to tokens that have exactly the provided scopes (no more, no less).
        This is useful for ensuring strict scope matching for tokens.

        Args:
            scope_string (str | list): Space-delimited string or list of scope names.

        Returns:
            TokenQuerySet: Queryset of tokens matching exactly the required scopes.
        """
        num_scopes = len(_process_scopes(scope_string))
        scopes_qs = (
            self.annotate(models.Count('scopes'))
            .require_scopes(scope_string)
            .filter(scopes__count=num_scopes)
            .values('pk', 'scopes__id')
        )
        pks = [v['pk'] for v in scopes_qs]
        return self.filter(pk__in=pks)

    def equivalent_to(self, token) -> 'TokenQuerySet':
        """
        Return a queryset of tokens that are equivalent to the given token.

        Tokens are considered equivalent if they:
        - Belong to the same character (character_id matches)
        - Have exactly the same scopes as the provided token
        - Are associated with the same user or are userless (user is null)
        - Are not the provided token itself (exclude pk)

        This is useful for finding duplicate or alternative tokens for a character
        with the same scope and user context.

        Args:
            token: The Token instance to compare against.

        Returns:
            TokenQuerySet: Queryset of equivalent Token instances.
        """
        return (
            self.filter(character_id=token.character_id)
            .require_scopes_exact(token.scopes.all())
            .filter(models.Q(user=token.user) | models.Q(user__isnull=True))
            .exclude(pk=token.pk)
        )


class TokenManager(models.Manager['Token']):
    def get_queryset(self) -> TokenQuerySet:
        """
        Return the default queryset for Token objects.

        This method overrides the default manager's get_queryset to return a TokenQuerySet,
        enabling custom queryset methods for Token model operations.
        """
        return TokenQuerySet(self.model, using=self._db)

    def create_from_request(self, request: HttpRequest):
        """
        Create a new Token instance from an HTTP request.

        This method handles the OAuth code exchange, validates the resulting JWT token,
        extracts character and scope information, and creates a new Token model instance.
        It also deduplicates tokens if configured, ensuring only one equivalent token exists
        per character, scope, and user context.

        Args:
            request (HttpRequest): The incoming HTTP request containing the OAuth code.

        Returns:
            Token: The created or deduplicated Token instance.
        """
        logger.debug(
            'Creating new token for %s session %s',
            request.user,
            request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
        )

        code = request.GET.get('code', None)
        if not code:
            msg = 'No code provided in request'
            raise ValueError(msg)

        token, token_data, token_detail = self._extract_and_validate_token(code)

        model = self.create(
            character_id=int(token_detail[2]),
            character_name=token_data['name'],
            character_owner_hash=token_data['owner'],
            access_token=token['access_token'],
            refresh_token=token.get('refresh_token', None),
            token_type=token_detail[0].lower(),
            user=request.user if request.user.is_authenticated else None,
        )

        self._add_scopes_to_model(model, token_data.get('scp', []))

        logger.debug('Added %d scopes to new token.', model.scopes.all().count())

        return self._deduplicate_token(model)

    def _extract_and_validate_token(self, code: str):
        """
        Exchange the provided OAuth code for an EVE Online SSO token, validate the JWT,
        and extract token details for further processing.

        This method performs the following steps:
        - Exchanges the authorization code for an access token using EVE SSO.
        - Validates the returned JWT access token.
        - Extracts token data and details (such as character ID and token type).

        Args:
            code (str): The OAuth authorization code received from EVE SSO.

        Returns:
            tuple: (token, token_data, token_detail)
                token (dict): The token response from EVE SSO.
                token_data (dict): Decoded JWT token data.
                token_detail (list): List of token details parsed from the JWT 'sub' field.

        Raises:
            ValueError: If no access token is returned or the token is invalid.
        """
        token = exchange_code_for_token(code)
        access_token = token.get('access_token', None)
        if not access_token:
            msg = 'No access token returned from SSO'
            raise ValueError(msg)
        if not validate_jwt_token(access_token):
            msg = 'Access token returned from SSO is invalid'
            raise ValueError(msg)
        token_data = validate_jwt_token(access_token)
        logger.debug('Token data: %s', token_data)
        token_detail = token_data.get('sub', '').split(':')
        return token, token_data, token_detail

    def _add_scopes_to_model(self, model, scopes):
        """
        Add ESI scopes to a Token model instance.

        This method takes a token model and a list (or string) of scope names, and associates
        each scope with the token. If a scope does not exist in the database, it creates a placeholder
        Scope object with a generated description. This ensures that all scopes from the token are
        represented in the model, even if they are new or missing from the database.

        Args:
            model: The Token model instance to associate scopes with.
            scopes: A list of scope names or a single scope string.
        """
        if isinstance(scopes, str):
            scopes = [scopes]
        for s in scopes:
            from apps.esi.models import Scope  # Avoid circular import  # noqa: PLC0415

            try:
                scope = Scope.objects.get(name=s)
                model.scopes.add(scope)
            except Scope.DoesNotExist:
                # Create a placeholder scope if missing
                try:
                    help_text = s.split('.')[1].replace('_', ' ').capitalize()
                except IndexError:
                    help_text = s.replace('_', ' ').capitalize()
                scope = Scope.objects.create(name=s, description=help_text)
                model.scopes.add(scope)

    def _deduplicate_token(self, model):
        """
        Deduplicate tokens for a character, scopes, and user context.

        This method checks for existing tokens that are equivalent to the provided model
        (same character, exact scopes, and same user or userless). If such tokens exist,
        it updates their access and refresh tokens with the new values and refreshes their
        creation timestamp. If an equivalent token exists for the same user, the new token
        is deleted and the existing token is returned. Otherwise, the new token is returned.

        This ensures that only one token per character, scope set, and user context exists,
        preventing unnecessary duplicates and keeping token data up to date.

        Args:
            model: The Token instance to deduplicate.

        Returns:
            Token: The deduplicated Token instance (either the updated existing token or the new one).
        """
        qs = self.get_queryset().equivalent_to(model)
        if qs.exists():
            logger.debug(
                'Identified %d tokens equivalent to new token. '
                'Updating access and refresh tokens.',
                qs.count(),
            )
            qs.update(
                access_token=model.access_token,
                refresh_token=model.refresh_token,
                created=timezone.now(),
            )
            if qs.filter(user=model.user).exists():
                model.delete()
                return qs.filter(user=model.user)[0]
        return model

    @staticmethod
    def validate_access_token(token: str) -> dict[str, Any] | None:
        """
        Validate a JWT access token retrieved from EVE SSO.

        This method attempts to decode and validate the provided JWT token using EVE SSO's
        public key. If successful, it extracts and returns token data including character ID
        and token type. If validation fails due to missing fields, decoding errors, or token
        expiration, it logs a warning and returns None.

        Args:
            token (str): The JWT access token to validate.

        Returns:
            dict[str, Any] | None: Decoded token data if valid, otherwise None.
        """
        try:
            token_data = validate_jwt_token(token)
            token_detail = token_data.get('sub').split(':')
            token_data['character_id'] = int(token_detail[2])
            token_data['token_type'] = token_detail[0].lower()
        except Exception as e:
            logger.warning('The JWT token is invalid: %s', e)
            return None
        else:
            return token_data
