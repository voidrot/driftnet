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
    tokens = (
        Token.objects.filter(user=request.user.id)
        .select_related('user')
        .prefetch_related('scopes')
    )
    character_list = [
        {
            'id': token.id,
            'user': token.user_id,
            'character_id': token.character_id,
            'character_name': getattr(token, 'character_name', ''),
            'scopes': list(token.scopes.values_list('name', flat=True)),
        }
        for token in tokens
    ]
    context = {
        'characters': character_list,
        'all_scopes': Scope.objects.all(),
    }
    logger.debug('loading with characters %s', character_list)
    return render(request, 'characters.html', context=context)


@login_required
def profile(request):
    """Render the user profile / account settings page."""
    return render(request, 'profile.html')


@login_required
def character_redirect(request):
    """Redirect to the character selection page."""
    # SECURITY: ensure that only valid scopes are allowed to be passes to the redirect
    allowed_scopes = set(
        Scope.objects.values_list('name', flat=True)
    )  # or a static set/list if appropriate
    requested_scopes = request.GET.get('scopes', '').split(' ')
    scopes = [scope for scope in requested_scopes if scope in allowed_scopes and scope]
    logger.debug(
        'Redirecting to character selection with validated scopes %s (original: %s)',
        scopes,
        requested_scopes,
    )
    return sso_redirect(request, scopes=scopes, return_to='users:characters')
    return sso_redirect(request, scopes=scopes, return_to='users:characters')
