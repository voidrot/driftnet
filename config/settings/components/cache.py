from environs import env
from environs import validate

CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env(
            'REDIS_APP_URL', default='redis://redis:6379/0', validate=validate.URL()
        ),
    },
    'esi': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env(
            'REDIS_ESI_URL', default='redis://redis:6379/0', validate=validate.URL()
        ),
        'TIMEOUT': None,
    },
}
