import logging

from celery import shared_task

from apps.shared.providers import esi

logger = logging.getLogger(__name__)


# No rate limit for this task since it is controlled by celery beat
@shared_task
def get_alliance_list():
    logger.info('Fetching alliance list')
    # Call the ESI provider to get the alliance list
    op = esi.client.Alliance.GetAlliances()
    res = op.results()  # Fix: use .results as a property, not a method
    logger.info('Fetched %d alliances', len(res))
    for alliance_id in res:
        get_alliance_info.delay(kwargs={'alliance_id': alliance_id})
        get_alliance_corporations.delay(kwargs={'alliance_id': alliance_id})


@shared_task(rate_limit='30/m')
def get_alliance_info(alliance_id: int):
    logger.info('Fetching info for alliance ID: %d', alliance_id)
    # Call the ESI provider to get the alliance info
    esi.client.Alliance.GetAlliancesAllianceId(alliance_id=alliance_id)
    logger.info('Fetched info for alliance ID: %d', alliance_id)


@shared_task(rate_limit='30/m')
def get_alliance_corporations(alliance_id):
    logger.info('Fetching corporations for alliance ID: %d', alliance_id)
    # Call the ESI provider to get the alliance corporations
    corporations = esi.client.Alliance.GetAlliancesAllianceIdCorporations(
        alliance_id=alliance_id
    )
    logger.info(
        'Fetched %d corporations for alliance ID: %d', len(corporations), alliance_id
    )


@shared_task
def get_alliance_icons():
    logger.info('Fetching alliance icons')
    # Call the ESI provider to get the alliance icons
    op = esi.client.Universe.GetAllianceIcons()
    res = op.results()  # Fix: use .results as a property, not a method
    logger.info('Fetched icons for %d alliances', len(res))
