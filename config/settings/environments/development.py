from config.env import env
from config.settings.components.installed_apps import INSTALLED_APPS
from config.settings.components.middleware import MIDDLEWARE

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='fQWTeeQDL8Ut202Tywwlt5nJkPvSgrkFDlJnypuc9ELPIzqWYL98ZDzsTHOJZL4v',  # pyright: ignore[reportArgumentType]
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']  # noqa: S104


CACHE = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env('REDIS_URL', default='redis://redis:6379/1'),  # pyright: ignore[reportArgumentType]
    }
}

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', default='mailpit')  # pyright: ignore[reportArgumentType]
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    *INSTALLED_APPS,
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE = [*MIDDLEWARE, 'debug_toolbar.middleware.DebugToolbarMiddleware']


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

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'django': {'level': 'INFO', 'handlers': ['console'], 'propagate': True},
        'apps.esi': {
            'level': env('APPS_ESI_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.users': {
            'level': env('APPS_USERS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.sde': {
            'level': env('APPS_SDE_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.esi_utils': {
            'level': env('APPS_ESI_UTILS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.dashboard': {
            'level': env('APPS_DASHBOARD_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.alliance': {
            'level': env('APPS_ALLIANCE_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.asset': {
            'level': env('APPS_ASSET_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.character': {
            'level': env('APPS_CHARACTER_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.clones': {
            'level': env('APPS_CLONES_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.contacts': {
            'level': env('APPS_CONTACTS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.contracts': {
            'level': env('APPS_CONTRACTS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.corporation': {
            'level': env('APPS_CORPORATIONS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.faction_warfare': {
            'level': env('APPS_FACTION_WARFARE_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.fittings': {
            'level': env('APPS_FITTINGS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.fleets': {
            'level': env('APPS_FLEETS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.incursions': {
            'level': env('APPS_INCURSIONS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.industry': {
            'level': env('APPS_INDUSTRY_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.insurance': {
            'level': env('APPS_INSURANCE_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.killmails': {
            'level': env('APPS_KILLMAILS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.location': {
            'level': env('APPS_LOCATION_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.loyalty': {
            'level': env('APPS_LOYALTY_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.mail': {
            'level': env('APPS_MAIL_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.market': {
            'level': env('APPS_MARKET_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.planetary_interaction': {
            'level': env('APPS_PLANETARY_INTERACTION_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.skills': {
            'level': env('APPS_SKILLS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.sovereignty': {
            'level': env('APPS_SOVEREIGNTY_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.wallet': {
            'level': env('APPS_WALLET_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.wars': {
            'level': env('APPS_WARS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'apps.server_status': {
            'level': env('APPS_SERVER_STATUS_LOG_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
