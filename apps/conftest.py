import os

import pytest
from zeal import zeal_context


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture(autouse=True)
def ensure_django_settings(monkeypatch):
    """Ensure DJANGO_SETTINGS_MODULE is set for tests.

    Tests expect Django settings to be available. pytest.ini sets
    DJANGO_SETTINGS_MODULE, but some runners or IDEs may not load that
    before importing. This fixture ensures the env var is present.
    """
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'


@pytest.fixture(autouse=True)
def use_zeal():
    with zeal_context():
        yield
