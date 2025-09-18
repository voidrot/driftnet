import logging

from celery import shared_task

from apps.alliance.models import Alliance
from apps.alliance.operations import _get_alliance_icon
from apps.alliance.operations import _get_alliance_info
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


# No rate limit for this task since it is controlled by celery beat
@shared_task
def get_alliance_list() -> None:
    logger.info('Fetching alliance list')
    # Call the ESI provider to get the alliance list
    op = esi.client.Alliance.GetAlliances()
    res = op.results()  # Fix: use .results as a property, not a method
    logger.info('Fetched %d alliances', len(res))
    for alliance_id in res:
        get_alliance_info.delay(alliance_id)
        get_alliance_corporations.delay(alliance_id)


@shared_task(rate_limit='30/m')
def get_alliance_info(alliance_id: int) -> None:
    _get_alliance_info(alliance_id)


@shared_task(rate_limit='30/m')
def get_alliance_corporations(alliance_id: int) -> None:
    logger.info('Fetching corporations for alliance ID: %d', alliance_id)
    # Call the ESI provider to get the alliance corporations
    op = esi.client.Alliance.GetAlliancesAllianceIdCorporations(alliance_id=alliance_id)
    res = op.result()  # Fix: use .results as a property, not a method
    logger.info('Fetched %d corporations for alliance ID: %d', len(res), alliance_id)


@shared_task
def get_alliance_icons() -> None:
    alliances = Alliance.objects.all().values_list('id', flat=True)
    for alliance_id in alliances:
        get_alliance_icon.delay(kwargs={'alliance_id': alliance_id})


@shared_task(rate_limit='30/m')
def get_alliance_icon(alliance_id: int) -> None:
    _get_alliance_icon(alliance_id)
