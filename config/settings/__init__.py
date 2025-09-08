from os import environ

from split_settings.tools import include
from split_settings.tools import optional

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/database.py',
    'components/celery.py',
    'components/auth.py',
    'components/cache.py',
    'components/logging.py',
    'components/security.py',
    # 'components/feature_flags.py',
    'components/sentry.py',
    'components/session.py',
    'components/static.py',
    'components/app_settings.py',
    'components/esi.py',
    f'environments/{ENV}.py',
    optional('environments/local.py'),
]

include(*base_settings)
