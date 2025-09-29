DJANGO_APPS = [
    'unfold',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.forms',
]

PROJECT_APPS = [
    'apps.sde',
    'apps.users',
    'apps.esi',
]

THIRD_PARTY_APPS = [
    # 'django_extensions',
    # 'django_cotton',
    'django_cotton.apps.SimpleAppConfig',
    'template_partials.apps.SimpleAppConfig',
    'django_htmx',
    'csp',
    'organizations',
    'allauth_ui',
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.usersessions',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.eveonline',
    'django_celery_results',
    'django_celery_beat',
    'crispy_forms',
    'widget_tweaks',
    'slippers',
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]
