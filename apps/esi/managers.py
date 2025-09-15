import logging
from datetime import timedelta
from typing import Any

from django.db import models
from django.http import HttpRequest
from django.utils import timezone

from apps.esi.app_settings import ESI_ALWAYS_CREATE_TOKEN
from apps.esi.app_settings import ESI_TOKEN_VALID_DURATION
from apps.esi.helpers import exchange_code_for_token
from apps.esi.helpers import validate_jwt_token

logger = logging.getLogger(__name__)


def _process_scopes(scopes) -> set[str]:
    if scopes is None:
        # support filtering by no scopes with None passed
        scopes = []
    if not isinstance(scopes, models.QuerySet) and len(scopes) == 1:
        # support a single space-delimited string inside a list because :users:
        scopes = scopes[0]
    # support space-delimited string scopes or lists
    if isinstance(scopes, str):
        scopes = set(scopes.split())
    return {str(s) for s in scopes}


class TokenQuerySet(models.QuerySet['Token']):  # pyright: ignore[reportUndefinedVariable]
    def get_expired_tokens(self) -> 'TokenQuerySet':
        """Return tokens that are expired or will expire in the next 5 minutes."""
        max_age = timezone.now() - timedelta(seconds=ESI_TOKEN_VALID_DURATION - 300)
        return self.filter(created__lte=max_age)

    def bulk_refresh_tokens(self) -> 'TokenQuerySet':
        """
        Refresh all expired tokens in the queryset.
        Also delete any tokens that can not be refreshed.
        """
        incomplete = []
        for model in self.filter(refresh_token__isnull=False):
            try:
                model.refresh()
                logger.debug(
                    'Refreshed token for character %s (%s)',
                    model.character_name,
                    model.character_id,
                )
            except Exception as e:  # pylint: disable=broad-except
                logger.exception(
                    'Failed to refresh token for character %s (%s): %s',
                    model.character_name,
                    model.character_id,
                    e,
                )
                incomplete.append(model.pk)
        self.filter(refresh_token__isnull=True).get_expired_tokens().delete()
        return self.exclude(pk__in=incomplete)

    def require_scopes(self, scope_string: str | list) -> 'TokenQuerySet':
        """
        Filter tokens that have all of the required scopes.
        """
        scopes = _process_scopes(scope_string)
        if not scopes:
            return self.filter(scopes__isnull=True)
        from .models import Scope  # Avoid circular import  # noqa: PLC0415

        scope_pks = Scope.objects.filter(name__in=scopes).values_list('pk', flat=True)
        if len(scopes) != len(scope_pks):
            # Some scopes do not exist, so no tokens can match
            return self.none()
        tokens = self.all()
        for pk in scope_pks:
            tokens = tokens.filter(scopes__id=pk)
        return tokens

    def require_scopes_exact(self, scope_string: str | list) -> 'TokenQuerySet':
        """
        Filter tokens which exactly have the given scopes.
        """
        num_scopes = len(_process_scopes(scope_string))
        scopes_qs = (
            self.annotate(models.Count('scopes'))
            .require_scopes(scope_string)
            .filter(scopes__count=num_scopes)
            .values('pk', 'scopes__id')
        )
        pks = [v['pk'] for v in scopes_qs]
        return self.filter(pk__in=pks)

    def equivalent_to(self, token) -> 'TokenQuerySet':
        """
        Fetch all tokens which match the character and scopes of given reference token
        """
        return (
            self.filter(character_id=token.character_id)
            .require_scopes_exact(token.scopes.all())
            .filter(models.Q(user=token.user) | models.Q(user__isnull=True))
            .exclude(pk=token.pk)
        )


class TokenManager(models.Manager['Token']):  # pyright: ignore[reportUndefinedVariable]
    def get_queryset(self) -> TokenQuerySet:
        return TokenQuerySet(self.model, using=self._db)

    def create_from_request(self, request: HttpRequest):
        logger.debug(
            'Creating new token for %s session %s',
            request.user,
            request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
        )

        code = request.GET.get('code', None)
        if not code:
            msg = 'No code provided in request'
            raise ValueError(msg)

        token = exchange_code_for_token(code)

        access_token = token.get('access_token', None)
        if not access_token:
            msg = 'No access token returned from SSO'
            raise ValueError(msg)

        token_data = validate_jwt_token(access_token)
        logger.debug('Token data: %s', token_data)
        token_detail = token_data.get('sub').split(':')

        model = self.create(
            character_id=int(token_detail[2]),
            character_name=token_data['name'],
            character_owner_hash=token_data['owner'],
            access_token=token['access_token'],
            refresh_token=token.get('refresh_token', None),
            token_type=token_detail[0].lower(),
            user=request.user if request.user.is_authenticated else None,
        )

        # parse scopes
        scopes = token_data.get('scp', [])

        # if a single scope is supplied its a string... recast to list
        if isinstance(scopes, str):
            scopes = [scopes]

        for s in scopes:
            from apps.esi.models import Scope  # Avoid circular import  # noqa: PLC0415

            try:
                scope = Scope.objects.get(name=s)
                model.scopes.add(scope)
            except Scope.DoesNotExist:
                # This scope isn't included in a data migration.
                # Create a placeholder until it updates.
                try:
                    help_text = s.split('.')[1].replace('_', ' ').capitalize()
                except IndexError:
                    # Unusual scope name, missing periods.
                    help_text = s.replace('_', ' ').capitalize()
                scope = Scope.objects.create(name=s, description=help_text)
                model.scopes.add(scope)
        logger.debug('Added %d scopes to new token.', model.scopes.all().count())

        if not ESI_ALWAYS_CREATE_TOKEN:
            # check if we already have a token with same scopes
            qs = self.get_queryset().equivalent_to(model)
            if qs.exists():
                logger.debug(
                    'Identified %d tokens equivalent to new token. '
                    'Updating access and refresh tokens.',
                    qs.count(),
                )
                qs.update(
                    access_token=model.access_token,
                    refresh_token=model.refresh_token,
                    created=timezone.now(),
                )
                if qs.filter(user=model.user).exists():
                    # If one of the equivalent tokens belongs to the same user,
                    # delete the new token and return the existing one.
                    model.delete()
                    model = qs.filter(user=model.user)[0]
        return model

    @staticmethod
    def validate_access_token(token: str) -> dict[str, Any] | None:
        """
        Validate a JWT retrieved from EVE SSO
        """
        try:
            token_data = validate_jwt_token(token)
            token_detail = token_data.get('sub').split(':')  # pyright: ignore[reportOptionalMemberAccess]
            token_data['character_id'] = int(token_detail[2])
            token_data['token_type'] = token_detail[0].lower()
            return token_data
        except Exception as e:
            logger.warning('The JWT token is invalid: %s', e)
            return None

    # @staticmethod
    # def _decode_jwt(
    #     jwt_token: str, jwk_set: dict, issuer: str | Iterable[str] | None
    # ) -> dict[str, Any]:
    #     """
    #     Decode JWT access token supplied by EVE SSO
    #     """
    #     logger.debug('Decoding JWT token')
    #     token_data = jwt.decode(
    #         jwt_token,
    #         jwk_set,
    #         algorithms=jwk_set['alg'],
    #         audience=ESI_TOKEN_JWT_AUDIENCE,
    #         issuer=issuer,
    #     )
    #     token_detail = token_data.get('sub').split(':')  # pyright: ignore[reportOptionalMemberAccess]
    #     token_data['character_id'] = int(token_detail[2])
    #     token_data['token_type'] = token_detail[0].lower()
    #     logger.debug('Decoded JWT token successfully: %s', token_data)
    #     return token_data

    # @staticmethod
    # def validate_access_token(token: str) -> dict[str, Any] | None:
    #     """
    #     Validate a JWT retrieved from EVE SSO
    #     """
    #     res = httpx.get(ESI_TOKEN_JWK_SET_URL)
    #     res.raise_for_status()
    #     data = res.json()

    #     try:
    #         jwk_sets = data.get('keys')
    #     except KeyError as e:
    #         logger.warning(
    #             'JWK Set response did not contain keys: %s\nPayload looks like %s',
    #             e,
    #             data,
    #         )
    #         return None
    #     jwk_set = [item for item in jwk_sets if item['alg'] == 'RS256'].pop()
    #     try:
    #         return TokenManager._decode_jwt(
    #             token, jwk_set, ('login.eveonline.com', 'https://login.eveonline.com')
    #         )
    #     except ExpiredSignatureError:
    #         logger.warning('The JWT token has expired')
    #         return None
    #     except JWTError as e:
    #         logger.warning('The JWT signature was invalid: %s', e)
    #         return None

    # def create_from_code(self, code, user=None) -> 'Token':
    #     """
    #     Perform OAuth code exchange to retrieve a token.
    #     :param code: OAuth grant code.
    #     :param user: User who will own token.
    #     :return: :class:`esi.models.Token`
    #     """

    #     # perform code exchange
    #     logger.debug('Creating new token from code %s', code[:-5])
    #     oauth = OAuth2Session(
    #         ESI_SSO_CLIENT_ID, redirect_uri=app_settings.ESI_SSO_CALLBACK_URL
    #     )
    #     token = oauth.fetch_token(
    #         ESI_TOKEN_URL, client_secret=settings.ESI_SSO_CLIENT_SECRET, code=code
    #     )

    #     token_data = TokenManager.validate_access_token(token.get('access_token', None))

    #     # translate returned data to a model
    #     model = self.create(
    #         character_id=token_data['character_id'],  # type: ignore  # noqa: PGH003
    #         character_name=token_data['name'],  # type: ignore  # noqa: PGH003
    #         character_owner_hash=token_data['owner'],  # type: ignore  # noqa: PGH003
    #         access_token=token['access_token'],  # type: ignore  # noqa: PGH003
    #         refresh_token=token['refresh_token'],  # type: ignore  # noqa: PGH003
    #         token_type=token_data['token_type'],  # type: ignore  # noqa: PGH003
    #         user=user,
    #     )

    #     # get scp (scopes) from token data
    #     token_data.get('scp', None)

    #     # parse scopes
    #     if 'scp' in token_data.get('scp', {}):
    #         from esi.models import Scope

    #         # if a single scope is supplied its a string... recast to list
    #         if isinstance(token_data['scp'], str):
    #             token_data['scp'] = [token_data['scp']]

    #         for s in token_data['scp']:
    #             try:
    #                 scope = Scope.objects.get(name=s)
    #                 model.scopes.add(scope)
    #             except Scope.DoesNotExist:
    #                 # This scope isn't included in a data migration.
    #                 # Create a placeholder until it updates.
    #                 try:
    #                     help_text = s.split('.')[1].replace('_', ' ').capitalize()
    #                 except IndexError:
    #                     # Unusual scope name, missing periods.
    #                     help_text = s.replace('_', ' ').capitalize()
    #                 scope = Scope.objects.create(name=s, help_text=help_text)
    #                 model.scopes.add(scope)
    #         logger.debug('Added %d scopes to new token.', model.scopes.all().count())

    #     if not ESI_ALWAYS_CREATE_TOKEN:
    #         # see if we already have a token for this character and scope combination
    #         # if so, we don't need a new one
    #         queryset = self.get_queryset().equivalent_to(model)
    #         if queryset.exists():
    #             logger.debug(
    #                 'Identified %d tokens equivalent to new token. '
    #                 'Updating access and refresh tokens.',
    #                 queryset.count(),
    #             )
    #             queryset.update(
    #                 access_token=model.access_token,
    #                 refresh_token=model.refresh_token,
    #                 created=model.created,
    #             )
    #             if queryset.filter(user=model.user).exists():
    #                 logger.debug(
    #                     'Equivalent token with same user exists. Deleting new token.'
    #                 )
    #                 model.delete()
    #                 model = queryset.filter(user=model.user)[0]  # pick one at random

    #     logger.debug('Successfully created %r for user %s', model, user)
    #     return model

    # def create_from_request(self, request: HttpRequest) -> 'Token':
    #     """
    #     Generate a token from the OAuth callback request. Must contain 'code' in GET.
    #     :param request: OAuth callback request.
    #     :return: :class:`esi.models.Token`
    #     """
    #     logger.debug(
    #         'Creating new token for %s session %s',
    #         request.user,
    #         request.session.session_key[:5],  # pyright: ignore[reportOptionalSubscript]
    #     )
    #     code = request.GET.get('code')
    #     # attach a user during creation for some functionality in a post_save created
    #     # receiver I'm working on elsewhere
    #     return self.create_from_code(
    #         code, user=request.user if request.user.is_authenticated else None
    #     )
