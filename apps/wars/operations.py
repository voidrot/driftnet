import logging

from apps.esi.decorators import wait_for_esi_errorlimit_reset
from apps.shared.providers import esi
from apps.wars.models import War

logger = logging.getLogger(__name__)


@wait_for_esi_errorlimit_reset()
def _get_war_details(war_id: int) -> None:
    logger.debug(f'Fetching war details for war ID {war_id} from ESI')
    op = esi.client.Wars.GetWarsWarId(war_id=war_id)
    res = op.result()

    logger.debug(f'Fetched war details: {res}')

    War.objects.update_or_create(
        id=war_id,
        defaults={
            'declared': res.declared,
            'started': res.started,
            'finished': res.finished,
            'mutual': res.mutual,
            'open_for_allies': res.open_for_allies,
            'retracted': res.retracted,
            'aggressor': dict(res.aggressor),
            'allies': [dict(ally) for ally in res.allies] if res.allies else [],
            'defender': dict(res.defender),
        }
    )
