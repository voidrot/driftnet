DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.forms',
]

PROJECT_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.sde.apps.SdeConfig',
]

THIRD_PARTY_APPS = [
    'django_tailwind_cli',
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
    'django_celery_results',
    'django_celery_beat',
]

INSTALLED_APPS = [*DJANGO_APPS, *THIRD_PARTY_APPS, *PROJECT_APPS]
