import logging

from celery import shared_task

from apps.esi.exceptions import HTTPCacheError
from apps.serverstatus.models import ServerStatus
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def fetch_server_status(self):
    """Query the EVE Online server status endpoint."""

    try:
        logger.debug('Fetching server status from ESI')
        op = esi.client.Status.GetStatus()
        response = op.result()
        logger.debug('Server status response: %s', response)
        ServerStatus(
            player_count=response.players,
            server_version=response.server_version,
            start_time=response.start_time,
            vip_mode=response.vip if response.vip is not None else False,
        ).save()
    except HTTPCacheError as e:
        logger.exception(
            'Failed getting cached data for 304 Not Modified Response: %s', e
        )
        raise self.retry(exc=e, countdown=60, max_retries=3) from e
