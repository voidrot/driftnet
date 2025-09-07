from config.env import APPS_DIR
from config.env import BASE_DIR
from config.env import env

DEBUG = env('DEBUG')
TEST = False

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        'DIRS': [str(APPS_DIR / 'templates')],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        'APP_DIRS': True,
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

ADMIN_URL = 'admin/'

ADMINS = [("""Buck Brady""", 'me@buckbrady.com')]

MANAGERS = ADMINS

TAILWIND_CLI_USE_DAISY_UI = True
TAILWIND_CLI_SRC_CSS = BASE_DIR / 'tailwind.css'
