from config.env import env
from config.settings.components.common import TEMPLATES
from config.settings.components.installed_apps import INSTALLED_APPS

DEBUG = False
TEST = True
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='CMzjhGlQSfERuyW2BR2ivPrHunBKtCr4dsiUZfocUySVF4326yzij9A0xhqoE3Gl',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

TEMPLATES[0]['OPTIONS']['debug'] = True

MEDIA_URL = 'http://media.testserver/'

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    *INSTALLED_APPS,
    'django_extensions',
]

CELERY_TASK_EAGER_PROPAGATES = True
