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
    'template_partials',
    'django_htmx',
    'csp',
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
    'django_celery_results',
    'django_celery_beat',
    "crispy_forms",
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]
