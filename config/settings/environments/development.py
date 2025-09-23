from environs import env

from config.settings.components.apps import DJANGO_APPS
from config.settings.components.apps import PROJECT_APPS
from config.settings.components.apps import THIRD_PARTY_APPS
from config.settings.components.common import DEBUG
from config.settings.components.logging import LOGGING
from config.settings.components.middleware import MIDDLEWARE
from config.settings.components.templates import TEMPLATES

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

TEMPLATES[0]['OPTIONS']['context_processors'].insert(
    0,
    'django.template.context_processors.debug',  # Make sure that we have debug context processor in development
)

THIRD_PARTY_APPS = [
    'django_tailwind_cli',
    'whitenoise.runserver_nostatic',
    *THIRD_PARTY_APPS,
    'debug_toolbar',
    'zeal',
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]

MIDDLEWARE = [
    *MIDDLEWARE,
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'zeal.middleware.zeal_middleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG,
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
        # Disable profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

CELERY_TASK_EAGER_PROPAGATES = True

LOGGING['loggers'] = {
    'django': {
        'level': env.log_level('DJANGO_LOG_LEVEL', default='INFO'),
        'handlers': ['console'],
        'propagate': True,
    },
    'apps.users': {
        'level': env.log_level('DJANGO_LOG_LEVEL', default='INFO'),
        'handlers': ['console'],
        'propagate': False,
    },
    'apps.esi': {
        'level': env.log_level('DJANGO_LOG_LEVEL', default='INFO'),
        'handlers': ['console'],
        'propagate': False,
    },
}
