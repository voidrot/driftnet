from config.settings.components.apps import DJANGO_APPS
from config.settings.components.apps import PROJECT_APPS
from config.settings.components.apps import THIRD_PARTY_APPS
from config.settings.components.middleware import MIDDLEWARE

TEST = True

THIRD_PARTY_APPS = [
    'whitenoise.runserver_nostatic',
    *THIRD_PARTY_APPS,
    'debug_toolbar',
    'zeal',
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]
MIDDLEWARE = [*MIDDLEWARE, 'zeal.middleware.zeal_middleware']