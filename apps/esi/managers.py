from datetime import timedelta
from django.db import models
import logging
from django.utils import timezone
from apps.esi import app_settings

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
        incomplete = []
        for model in self.filter(refresh_token__isnull=False):
            try:
                model.refresh()
                logger.debug(
                    'Refreshed token for character %s (%s)',
                    model.character_name,
                    model.character_id,
                )
            except Exception as e:
                logger.exception(
                    'Failed to refresh token for character %s (%s): %s',
                    model.character_name,
                    model.character_id,
                    e,
                )
                incomplete.append(model.pk)
        self.filter(refresh_token__isnull=False).get_expired_tokens().delete()
        return self.exclude(pk__in=incomplete)

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
    pass
