from environs import env

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', default='driftnet'),
        'USER': env.str('POSTGRES_USER', default='driftnet'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', default='driftnet'),
        'HOST': env.str('POSTGRES_HOST', default='localhost'),
        'PORT': env.str('POSTGRES_PORT', default='5432'),
        'OPTIONS': {
            'pool': env.bool('POSTGRES_POOL', default=True),
        },
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
