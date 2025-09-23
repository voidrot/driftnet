DJANGO_APPS = [
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
    'apps.users',
    'apps.esi',
]

THIRD_PARTY_APPS = [
    'csp',
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
    'django_celery_results',
    'django_celery_beat',
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]
