import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from esi.models import Scope
from esi.models import Token
from esi.views import sso_redirect


@require_POST
@login_required
def character_delete(request, character_id):
    """Delete the token for the given character and user."""
    token = get_object_or_404(Token, character_id=character_id, user=request.user)
    token.delete()
    return redirect('users:characters')


logger = logging.getLogger(__name__)


@login_required
def characters(request):
    """Render the user's EVE Online characters page."""
    context = {
        'characters': Token.objects.filter(user=request.user.id),
        'all_scopes': Scope.objects.all(),
    }
    logger.debug('loading with characters %s', context['characters'])
    return render(request, 'characters.html', context=context)


@login_required
def profile(request):
    """Render the user profile / account settings page."""
    return render(request, 'profile.html')


@login_required
def character_redirect(request, scopes=None):
    """Redirect to the character selection page."""
    return sso_redirect(request, scopes=scopes, return_to='users:characters')
