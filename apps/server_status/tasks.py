import logging

from celery import shared_task

from apps.server_status.models import ServerStatus
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


@shared_task()
def fetch_server_status():
    """Query the EVE Online server status endpoint."""

    logger.debug('Fetching server status from ESI')
    op = esi.client.Status.GetStatus()
    response = op.result()
    logger.debug('Server status response: %s', response)
    ServerStatus(
        player_count=response.players,  # pyright: ignore[reportAttributeAccessIssue]
        server_version=response.server_version,  # pyright: ignore[reportAttributeAccessIssue]
        start_time=response.start_time,  # pyright: ignore[reportAttributeAccessIssue]
        vip_mode=response.vip,  # pyright: ignore[reportAttributeAccessIssue]
    ).save()
