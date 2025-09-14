import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.http import require_POST

from apps.esi.models import Scope
from apps.esi.models import Token
from apps.esi.views import sso_redirect

logger = logging.getLogger(__name__)


@require_POST
@login_required
def character_delete(request, character_id, token_id):
    """Delete the token for the given character and user."""
    token = get_object_or_404(
        Token, character_id=character_id, user=request.user, id=token_id
    )
    token.delete()
    return redirect('users:characters')


logger = logging.getLogger(__name__)


@login_required
def characters(request):
    """Render the user's EVE Online characters page."""
    context = {
        'characters': Token.objects.filter(user=request.user.id).only(
            'id', 'user', 'character_id'
        ),
        'all_scopes': Scope.objects.all(),
    }
    logger.debug('loading with characters %s', context['characters'])
    return render(request, 'characters.html', context=context)


@login_required
def profile(request):
    """Render the user profile / account settings page."""
    return render(request, 'profile.html')


@login_required
def character_redirect(request):
    """Redirect to the character selection page."""
    scopes = request.GET.get('scopes').split(' ')
    logger.debug('Redirecting to character selection with scopes %s', scopes)
    return sso_redirect(request, scopes=scopes, return_to='users:characters')
