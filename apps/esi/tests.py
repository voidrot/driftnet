import random
import string
from unittest import mock

import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.esi import app_settings
from apps.esi import client
from apps.esi.managers import TokenManager
from apps.esi.managers import TokenQuerySet
from apps.esi.managers import _process_scopes
from apps.esi.models import Scope
from apps.esi.models import Token


@pytest.fixture
def scope_factory(db):
    def make_scope(name=None, description=None):
        name = name or ''.join(random.choices(string.ascii_lowercase, k=8))
        description = description or f'desc for {name}'
        return Scope.objects.create(name=name, description=description)

    return make_scope


@pytest.fixture
def token_factory(db, scope_factory):
    def make_token(**kwargs):
        User = get_user_model()
        user = kwargs.pop('user', None)
        if user is None:
            uname = 'testuser_' + ''.join(
                random.choices(string.ascii_lowercase + string.digits, k=8)
            )
            user = User.objects.create(username=uname)
        defaults = {
            'character_id': random.randint(1, 999999),
            'character_name': 'TestChar',
            'character_owner_hash': 'ownerhash',
            'access_token': 'token',
            'refresh_token': 'refresh',
            'token_type': 'character',
            'user': user,
        }
        defaults.update(kwargs)
        token = Token.objects.create(**defaults)
        # If 'created' is provided, update and save it
        if 'created' in kwargs:
            token.created = kwargs['created']
            token.save(update_fields=['created'])
        scopes = kwargs.get('scopes', [])
        for s in scopes:
            if isinstance(s, Scope):
                token.scopes.add(s)
            else:
                token.scopes.add(scope_factory(name=s))
        return token

    return make_token


class TestESIClientHelpers:
    def test_get_user_agent(self) -> None:
        ua = client._get_user_agent()
        assert app_settings.ESI_CONTACT_EMAIL in ua
        assert app_settings.ESI_APP_NAME in ua
        assert app_settings.ESI_APP_VERSION in ua
        if app_settings.ESI_APP_URL:
            assert app_settings.ESI_APP_URL in ua
            assert (
                ua
                == f'{app_settings.ESI_APP_NAME}/{app_settings.ESI_APP_VERSION} {app_settings.ESI_CONTACT_EMAIL} (+{app_settings.ESI_APP_URL})'
            )
        else:
            assert (
                ua
                == f'{app_settings.ESI_APP_NAME}/{app_settings.ESI_APP_VERSION} {app_settings.ESI_CONTACT_EMAIL}'
            )


class DummyToken:
    def __init__(
        self,
        character_id=1,
        user=None,
        scopes=None,
        pk=1,
        character_name='Test',
        character_owner_hash='owner',
        access_token='token',
        refresh_token='refresh',
        token_type='character',
    ):
        self.character_id = character_id
        self.user = user
        self.scopes = scopes or []
        self.pk = pk
        self.character_name = character_name
        self.character_owner_hash = character_owner_hash
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.created = timezone.now()

    def refresh(self):
        self.access_token = 'new_token'


def test_process_scopes_none():
    assert _process_scopes(None) == set()


def test_process_scopes_space_delimited():
    assert _process_scopes('a b c') == {'a', 'b', 'c'}


def test_process_scopes_list_single_string():
    assert _process_scopes(['a b']) == {'a', 'b'}


def test_process_scopes_list_multiple():
    assert _process_scopes(['a', 'b']) == {'a', 'b'}


@pytest.mark.django_db
def test_get_expired_tokens(token_factory):
    from apps.esi.managers import TokenQuerySet

    expired = token_factory(created=timezone.now() - timezone.timedelta(seconds=2000))
    valid = token_factory(created=timezone.now())
    qs = TokenQuerySet(model=type(expired), using='default').filter(
        pk__in=[expired.pk, valid.pk]
    )
    result = qs.get_expired_tokens()
    assert expired.pk in [t.pk for t in result]
    assert valid.pk not in [t.pk for t in result]


@pytest.mark.django_db
def test_bulk_refresh_tokens(token_factory):
    t1 = token_factory(refresh_token='r1')
    t2 = token_factory(refresh_token='r2')
    with mock.patch.object(type(t1), 'refresh', side_effect=[None, Exception('fail')]):
        qs = TokenQuerySet(model=type(t1), using='default').filter(
            pk__in=[t1.pk, t2.pk]
        )
    refreshed = qs.bulk_refresh_tokens()
    assert t2.pk not in [t.pk for t in refreshed]


@pytest.mark.django_db
def test_require_scopes(token_factory, scope_factory):
    s1 = scope_factory(name='scope1')
    s2 = scope_factory(name='scope2')
    t = token_factory()
    t.scopes.add(s1, s2)
    qs = TokenQuerySet(model=type(t), using='default').filter(pk=t.pk)
    filtered = qs.require_scopes(['scope1', 'scope2'])
    assert t.pk in [x.pk for x in filtered]


@pytest.mark.django_db
def test_require_scopes_exact(token_factory, scope_factory):
    s1 = scope_factory(name='scope1')
    t = token_factory()
    t.scopes.add(s1)
    qs = TokenQuerySet(model=type(t), using='default').filter(pk=t.pk)
    filtered = qs.require_scopes_exact(['scope1'])
    assert t.pk in [x.pk for x in filtered]


@pytest.mark.django_db
def test_equivalent_to(token_factory, scope_factory):
    s1 = scope_factory(name='scope1')
    # Use the same user for both tokens
    user = token_factory().user
    t1 = token_factory(character_id=1, user=user)
    t2 = token_factory(character_id=1, user=user)
    t1.scopes.add(s1)
    t2.scopes.add(s1)
    qs = TokenQuerySet(model=type(t1), using='default').filter(pk__in=[t1.pk, t2.pk])
    eq = qs.equivalent_to(t1)
    assert t2.pk in [x.pk for x in eq]


def test_validate_access_token_valid():
    with mock.patch(
        'apps.esi.managers.validate_jwt_token',
        return_value={'sub': 'character:char:123', 'owner': 'owner', 'name': 'Test'},
    ):
        result = TokenManager.validate_access_token('token')
        assert result['character_id'] == 123
        assert result['token_type'] == 'character'


def test_validate_access_token_invalid():
    with mock.patch(
        'apps.esi.managers.validate_jwt_token', side_effect=Exception('fail')
    ):
        result = TokenManager.validate_access_token('token')
        assert result is None
