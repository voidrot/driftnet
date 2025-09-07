from config.env import env
from config.settings.components.installed_apps import INSTALLED_APPS
from config.settings.components.middleware import MIDDLEWARE

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='fQWTeeQDL8Ut202Tywwlt5nJkPvSgrkFDlJnypuc9ELPIzqWYL98ZDzsTHOJZL4v',
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']  # noqa: S104


# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', default='mailpit')
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
