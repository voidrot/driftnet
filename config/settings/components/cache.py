from environs import env
from environs import validate

CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env.str(
            'REDIS_APP_URL', default='redis://redis:6379/0'
        ),
    },
    'esi': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env.str(
            'REDIS_ESI_URL', default='redis://redis:6379/0'
        ),
        'TIMEOUT': None,
    },
}
