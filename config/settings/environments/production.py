from environs import env
from config.settings.components.apps import DJANGO_APPS, PROJECT_APPS, THIRD_PARTY_APPS

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

THIRD_PARTY_APPS = [
    'whitenoise',
    *THIRD_PARTY_APPS,
]

INSTALLED_APPS = [*DJANGO_APPS, *PROJECT_APPS, *THIRD_PARTY_APPS]

# === AllAuth Settings ===
ACCOUNT_EMAIL_VERIFICATION = 'required'
