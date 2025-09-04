from config.env import BASE_DIR, APPS_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='hotshot'),
        'USER': env('POSTGRES_USER', default='hotshot'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='hotshotpass'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FIXTURE_DIRS = (str(APPS_DIR / 'fixtures'),)
