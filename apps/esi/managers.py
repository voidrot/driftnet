from datetime import timedelta
from django.db import models
import logging
from django.utils import timezone
from apps.esi import app_settings

logger = logging.getLogger(__name__)

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

class TokenManager(models.Manager):
    pass
