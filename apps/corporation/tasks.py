import logging

from celery import shared_task

from apps.corporation.models import Corporation
from apps.corporation.operations import _get_corporation_alliance_history
from apps.corporation.operations import _get_corporation_icon
from apps.corporation.operations import _get_corporation_info
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


@shared_task
def update_corporation_info() -> None:
    """
    Gather known corporation IDs and dispatch tasks to fetch their info.
    """
    op = esi.client.Corporation.GetCorporationsNpccorps()
    res = op.results()
    logger.info('Fetched %d NPC corporations from ESI', len(res))
    corporation_ids_from_db = Corporation.objects.values_list('id', flat=True)
    corporation_ids = list(set(res + corporation_ids_from_db))
    for corporation_id in corporation_ids:
        get_corporation_info.delay(corporation_id)


@shared_task(rate_limit='30/m')
def get_corporation_info(corporation_id: int) -> None:
    """
    Placeholder task to fetch and update corporation info by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch info for.
    """
    logger.info('Fetching info for corporation ID: %d', corporation_id)
    _get_corporation_info(corporation_id)


@shared_task
def get_corporation_icons() -> None:
    """
    Placeholder task to fetch and update corporation icons.
    """
    # Get all corporation IDs from the database
    corporation_ids = Corporation.objects.values_list('id', flat=True)
    for corporation_id in corporation_ids:
        update_corporation_icon.delay(corporation_id)


@shared_task(rate_limit='30/m')
def update_corporation_icon(corporation_id: int) -> None:
    """
    Placeholder task to fetch and update corporation icon by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch icon for.
    """
    logger.info('Fetching icon for corporation ID: %d', corporation_id)
    _get_corporation_icon(corporation_id)


@shared_task
def get_corporation_alliance_history() -> None:
    """
    Placeholder task to fetch and log corporation alliance history by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch alliance history for.
    """
    corporation_ids = Corporation.objects.values_list('id', flat=True)
    for corporation_id in corporation_ids:
        update_corporation_alliance_history.delay(corporation_id)


@shared_task(rate_limit='30/m')
def update_corporation_alliance_history(corporation_id: int) -> None:
    logger.info('Fetching alliance history for corporation ID: %d', corporation_id)
    _get_corporation_alliance_history(corporation_id)
