import functools
import logging
import time
from functools import wraps

from django.core.cache import cache

from apps.esi.rate_limiting import ESIRateLimitBucket
from apps.esi.rate_limiting import ESIRateLimits

from .models import CallbackRedirect
from .models import Token

logger = logging.getLogger(__name__)


def _check_callback(request) -> Token | None:
    # ensure session installed in database
    if not request.session.exists(request.session.session_key):
        logger.debug('Creating new session for %s', request.user)
        request.session.create()

    # clean up callback redirect, pass token if new requested
    try:
        model = CallbackRedirect.objects.get(session_key=request.session.session_key)
        token = Token.objects.get(pk=model.token.pk)
        model.delete()
        logger.debug(
            'Retrieved new token from callback for %s session %s',
            request.user,
            request.session.session_key[:5],
        )
        return token

    except (CallbackRedirect.DoesNotExist, Token.DoesNotExist, AttributeError):
        logger.debug(
            'No callback for %s session %s',
            request.user,
            request.session.session_key[:5],
            exc_info=True,
        )
        return None


def tokens_required(scopes='', new=False):
    """
    Decorator for views to request an ESI Token.
    Accepts required scopes as a space-delimited string
    or list of strings of scope names.
    Can require a new token to be retrieved by SSO.
    Returns a QueryDict of Tokens.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # if we're coming back from SSO with a new token, return it
            token = _check_callback(request)
            if token:
                tokens = Token.objects.filter(pk=token.pk)
                logger.debug('Returning new token.')
                return view_func(request, tokens, *args, **kwargs)

            if not new:
                # ensure user logged in to check existing tokens
                if not request.user.is_authenticated:
                    logger.debug(
                        'Session %s is not logged in. Redirecting to login.',
                        request.session.session_key[:5],
                    )
                    from django.contrib.auth.views import redirect_to_login

                    return redirect_to_login(request.get_full_path())

                # collect tokens in db, check if still valid, return if any
                tokens = (
                    Token.objects.filter(user__pk=request.user.pk)
                    .require_scopes(scopes)
                    .require_valid()
                )
                if tokens.exists():
                    logger.debug(
                        'Retrieved %s tokens for %s session %s',
                        tokens.count(),
                        request.user,
                        request.session.session_key[:5],
                    )
                    return view_func(request, tokens, *args, **kwargs)

            # trigger creation of new token via sso
            logger.debug(
                'No tokens identified for %s session %s. Redirecting to SSO.',
                request.user,
                request.session.session_key[:5],
            )
            from esi.views import sso_redirect

            return sso_redirect(request, scopes=scopes)

        return _wrapped_view

    return decorator


def token_required(scopes='', new=False):
    """
    Decorator for views which supplies a single,
    user-selected token for the view to process.
    Same parameters as tokens_required.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # if we're coming back from SSO with a new token, return it
            token = _check_callback(request)
            if token:
                logger.debug(
                    'Got new token from %s session %s. Returning to view.',
                    request.user,
                    request.session.session_key[:5],
                )
                return view_func(request, token, *args, **kwargs)

            # if we're selecting a token, return it
            if request.method == 'POST':
                if request.POST.get('_add', False):
                    logger.debug(
                        '%s has selected to add new token. Redirecting to SSO.',
                        request.user,
                    )
                    # user has selected to add a new token
                    from esi.views import sso_redirect

                    return sso_redirect(request, scopes=scopes)

                token_pk = request.POST.get('_token', None)
                if token_pk:
                    logger.debug('%s has selected token %s', request.user, token_pk)
                    try:
                        token = Token.objects.get(pk=token_pk)
                        # ensure token belongs to this user and has required scopes
                        if (
                            (token.user and token.user == request.user)
                            or not token.user
                        ) and Token.objects.filter(pk=token_pk).require_scopes(
                            scopes
                        ).require_valid().exists():
                            logger.debug(
                                'Selected token fulfills requirements of view. '
                                'Returning.'
                            )
                            return view_func(request, token, *args, **kwargs)

                    except Token.DoesNotExist:
                        logger.debug('Token %s not found.', token_pk)

            if not new:
                # present the user with token choices
                tokens = (
                    Token.objects.filter(user__pk=request.user.pk)
                    .require_scopes(scopes)
                    .require_valid()
                )
                if tokens.exists():
                    logger.debug(
                        'Returning list of available tokens for %s.', request.user
                    )
                    from esi.views import select_token

                    return select_token(request, scopes=scopes, new=new)
                logger.debug(
                    'No tokens found for %s session %s with scopes %s',
                    request.user,
                    request.session.session_key[:5],
                    scopes,
                )

            # prompt the user to add a new token
            logger.debug(
                'Redirecting %s session %s to SSO.',
                request.user,
                request.session.session_key[:5],
            )
            from esi.views import sso_redirect

            return sso_redirect(request, scopes=scopes)

        return _wrapped_view

    return decorator


def single_use_token(scopes='', new=False):
    """
    Decorator for views which supplies a single use token granted via sso login
    regardless of login state.
    Same parameters as tokens_required.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # if we're coming back from SSO for a new token, return it
            token = _check_callback(request)
            if token:
                logger.debug(
                    'Got new token from session %s. Returning to view.',
                    request.session.session_key[:5],
                )
                return view_func(request, token, *args, **kwargs)

            # prompt the user to login for a new token
            logger.debug(
                'Redirecting session %s to SSO.', request.session.session_key[:5]
            )
            from esi.views import sso_redirect

            return sso_redirect(request, scopes=scopes)

        return _wrapped_view

    return decorator


def wait_for_esi_errorlimit_reset(cache_key='esi_error_limit_reset', poll_interval=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            reset = cache.get(cache_key)
            if reset is not None:
                while cache.get(cache_key):
                    time.sleep(poll_interval)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def esi_rate_limiter_bucketed(
    bucket: ESIRateLimitBucket,
    raise_on_limit: bool = True,
):
    # TODO Investigate esi cache hits.

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ESIRateLimits.check_bucket(bucket, raise_on_limit)
            return func(*args, **kwargs)

        return wrapper

    return decorator
