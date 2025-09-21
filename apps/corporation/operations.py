import logging

from apps.corporation.models import Corporation
from apps.corporation.models import CorporationAllianceHistory
from apps.corporation.models import CorporationIcon
from apps.esi.decorators import wait_for_esi_errorlimit_reset
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


@wait_for_esi_errorlimit_reset()
def _get_corporation_info(corporation_id: int) -> None:
    """
    Placeholder function to fetch and update corporation info by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch info for.
    """
    op = esi.client.Corporation.GetCorporationsCorporationId(
        corporation_id=corporation_id
    )
    res = op.result()
    logger.info('Fetched info for corporation ID: %d', corporation_id)
    logger.debug('Corporation info: %s', res)
    Corporation.objects.update_or_create(
        id=corporation_id,
        defaults={
            'name': res.name,
            'ticker': res.ticker,
            'ceo_id': res.ceo_id,
            'member_count': res.member_count,
            'alliance_id': res.alliance_id if res.alliance_id is not None else None,
            'description': res.description if res.description is not None else None,
            'url': res.url if res.url is not None else None,
            'tax_rate': res.tax_rate,
            'date_founded': res.date_founded if res.date_founded is not None else None,
            'creator_id': res.creator_id,
            'home_station_id': res.home_station_id
            if res.home_station_id is not None
            else None,
            'faction_id': res.faction_id if res.faction_id is not None else None,
            'shares': res.shares if res.shares is not None else None,
            'war_eligible': res.war_eligible if res.war_eligible is not None else False,
        },
    )
    logger.info('Updated corporation ID: %d in database', corporation_id)


@wait_for_esi_errorlimit_reset()
def _get_corporation_icon(corporation_id: int) -> None:
    """
    Placeholder function to fetch and update corporation icon by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch icon for.
    """
    op = esi.client.Corporation.GetCorporationsCorporationIdIcons(
        corporation_id=corporation_id
    )
    res = op.result()
    # Assuming CorporationIcon model exists and has a OneToOne relationship with Corporation
    CorporationIcon.objects.update_or_create(
        corporation_id=corporation_id,
        defaults={
            'px64x64': res.px64x64,
            'px128x128': res.px128x128,
        },
    )
    logger.info('Updated icon for corporation ID: %d in database', corporation_id)


@wait_for_esi_errorlimit_reset()
def _get_corporation_alliance_history(corporation_id: int) -> None:
    """
    Placeholder function to fetch and log corporation alliance history by ID.

    Parameters:
        corporation_id (int): The ID of the corporation to fetch alliance history for.
    """
    op = esi.client.Corporation.GetCorporationsCorporationIdAlliancehistory(
        corporation_id=corporation_id
    )
    res = op.results()
    logger.info('Fetched alliance history for corporation ID: %d', corporation_id)
    logger.debug('Alliance history: %s', res)
    for record in res:
        CorporationAllianceHistory.objects.update_or_create(
            corporation_id=corporation_id,
            alliance_id=record.alliance_id if record.alliance_id is not None else None,
            record_id=record.record_id,
            defaults={
                'start_date': record.start_date,
                'is_deleted': record.is_deleted
                if record.is_deleted is not None
                else False,
            },
        )
    logger.info(
        'Updated alliance history for corporation ID: %d in database', corporation_id
    )
