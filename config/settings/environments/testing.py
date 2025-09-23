from config.settings.components.apps import INSTALLED_APPS
from config.settings.components.middleware import MIDDLEWARE

TEST = True

INSTALLED_APPS.append('zeal')
MIDDLEWARE.append('zeal.middleware.zeal_middleware')
