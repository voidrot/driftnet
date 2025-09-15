import logging

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from apps.esi.helpers import generate_sso_redirect
from apps.esi.models import CallbackRedirect
from apps.esi.models import Token

logger = logging.getLogger(__name__)


def sso_redirect(
    request: HttpRequest, scopes=None, return_to='/user/characters'
) -> HttpResponse:
    """
    Redirect the user to the EVE SSO login page with the appropriate parameters.

    If scopes are provided, they should be a space-separated string of scopes.
    """
    logger.debug(
        'Initiating redirect of %s session %s',
        request.user,
        request.session.session_key[:5] if request.session.session_key else '[no key]',
    )
    if scopes is None:
        scopes = []

    if request.session.session_key:
        CallbackRedirect.objects.filter(
            session_key=request.session.session_key
        ).delete()

    if not request.session.exists(request.session.session_key):  # pyright: ignore[reportArgumentType]
        request.session.create()
        logger.debug(
            'Created new session for %s: %s',
            request.user,
            request.session.session_key[:5]
            if request.session.session_key
            else '[no key]',
        )

    url = reverse(return_to) if return_to else request.get_full_path()

    redirect_url, state = generate_sso_redirect(scopes, url)

    CallbackRedirect.objects.create(
        session_key=request.session.session_key,
        state=state,
        url=url,
        scopes=','.join(scopes),
    )

    logger.debug(
        'Redirecting %s session %s to SSO. Callback will be redirected to %s',
        request.user,
        request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
        url,
    )

    return redirect(redirect_url)


def receive_callback(request: HttpRequest) -> HttpResponse:
    """
    Handle the callback from the EVE SSO login page.
    """
    logger.debug(
        'Received callback for %s session %s',
        request.user,
        request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
    )

    code = request.GET.get('code', None)
    state = request.GET.get('state', None)

    if not code or not state:
        logger.warning(
            'Callback missing code or state for %s session %s',
            request.user,
            request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
        )
        return HttpResponseBadRequest()

    callback = get_object_or_404(
        CallbackRedirect, state=state, session_key=request.session.session_key
    )

    token = Token.objects.create_from_request(request)
    callback.token = token
    callback.save()
    logger.debug(
        'Processed callback for %s session %s. Redirecting to %s',
        request.user,
        request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
        callback.url,
    )
    return redirect(callback.url)
