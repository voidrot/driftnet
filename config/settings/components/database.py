from config.env import APPS_DIR
from config.env import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='hotshot'),  # pyright: ignore[reportArgumentType]
        'USER': env('POSTGRES_USER', default='hotshot'),  # pyright: ignore[reportArgumentType]
        'PASSWORD': env('POSTGRES_PASSWORD', default='hotshotpass'),  # pyright: ignore[reportArgumentType]
        'HOST': env('POSTGRES_HOST', default='localhost'),  # pyright: ignore[reportArgumentType]
        'PORT': env('POSTGRES_PORT', default='5432'),  # pyright: ignore[reportArgumentType]
        "OPTIONS": {
            "pool": True,
        },
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FIXTURE_DIRS = (str(APPS_DIR / 'fixtures'),)
