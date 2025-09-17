import logging

from apps.esi.decorators import wait_for_esi_errorlimit_reset
from apps.shared.providers import esi

logger = logging.getLogger(__name__)


@wait_for_esi_errorlimit_reset()
def _get_alliance_info(alliance_id: int):
    """Helper function to get alliance info from ESI."""
    logger.info('Fetching info for alliance ID: %d', alliance_id)
    # Call the ESI provider to get the alliance info
    op = esi.client.Alliance.GetAlliancesAllianceId(alliance_id=alliance_id)
    op.result()
    logger.info('Fetched info for alliance ID: %d', alliance_id)
