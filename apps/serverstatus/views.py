import logging

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.serverstatus.models import ServerStatus

logger = logging.getLogger(__name__)


@require_GET
def current_status(request: HttpRequest) -> HttpResponse:
    ctx = {
        'server_status': {
            'text': 'Offline',
            'color': 'red',
        },
        'current_players': 0,
        'player_count_color': 'red',
    }
    server_status = ServerStatus.objects.first()
    if server_status is None:
        logger.error('No server status found in database')
    else:
        if server_status.player_count < 15000:
            ctx['player_count_color'] = 'red'
        elif server_status.player_count < 20000:
            ctx['player_count_color'] = 'orange'
        else:
            ctx['player_count_color'] = 'green'
        ctx['current_players'] = server_status.player_count
        if server_status.vip_mode:
            ctx['server_status']['text'] = 'VIP Mode'
            ctx['server_status']['color'] = 'orange'
            ctx['current_players'] = server_status.player_count
        else:
            ctx['server_status']['text'] = 'Online'
            ctx['server_status']['color'] = 'green'
            ctx['current_players'] = server_status.player_count
    return render(request, 'current-players.html', context=ctx)
