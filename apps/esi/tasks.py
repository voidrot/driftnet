import logging
from datetime import timedelta
from math import ceil

from celery import shared_task
from django.utils import timezone

from apps.esi.models import CallbackRedirect
from apps.esi.models import Token

logger = logging.getLogger(__name__)


@shared_task
def cleanup_callbackredirect(max_age=300):
    """
    Cleans up old callback redirects older than max_age seconds.
    """
    max_age = timezone.now() - timedelta(seconds=max_age)
    logger.debug(
        'Deleting all callback redirects created before %s',
        max_age.strftime('%b %d %Y %H:%M:%S'),
    )
    CallbackRedirect.objects.filter(created__lte=max_age).delete()


@shared_task
def cleanup_token() -> None:
    """
    Delete Orphaned Tokens, then refresh or delete expired :model:`esi.Token` models.
    """
    orphaned_tokens = Token.objects.filter(user__isnull=True)
    if orphaned_tokens.exists():
        logger.info('Deleting %d orphaned tokens.', orphaned_tokens.count())
        orphaned_tokens.delete()

    expired_tokens = Token.objects.exclude(user__isnull=True).get_expired_tokens()
    if expired_tokens.exists():
        logger.info(
            'Triggering bulk refresh of %d expired tokens.', expired_tokens.count()
        )
        for token_pk in expired_tokens.filter(refresh_token__isnull=False).values_list(
            'pk', flat=True
        ):
            refresh_or_delete_token.apply_async(args=[token_pk], priority=8)


@shared_task
def cleanup_token_subset(fraction: int = 48) -> None:
    """
    Delete Orphaned Tokens, then refresh or delete a subset of expired :model:`esi.Token` models.

    This task operates on 1/fraction of the oldest tokens and can be called on a more regular schedule
    """
    orphaned_tokens = Token.objects.filter(user__isnull=True)
    if orphaned_tokens.exists():
        logger.info('Deleting %d orphaned tokens.', orphaned_tokens.count())
        orphaned_tokens.delete()

    expired_tokens = Token.objects.exclude(user__isnull=True).get_expired_tokens()
    expired_tokens_subset = expired_tokens.filter(refresh_token__isnull=False).order_by(
        'created'
    )[: ceil(expired_tokens.count() / fraction)]

    if expired_tokens.exists():
        logger.info(
            f'Triggering bulk refresh of subset/possible {expired_tokens_subset.count()}/{expired_tokens.count()} expired tokens.'
        )
        for token_pk in expired_tokens_subset.values_list('pk', flat=True):
            refresh_or_delete_token.apply_async(args=[token_pk], priority=8)


@shared_task
def refresh_or_delete_token(token_pk: int):
    token = Token.objects.get(pk=token_pk)
    token.refresh_or_delete()
