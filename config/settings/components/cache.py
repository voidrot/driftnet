from environs import env

CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env.str('REDIS_APP_URL', default='redis://redis:6379/0'),
    },
    'esi': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env.str('REDIS_ESI_URL', default='redis://redis:6379/0'),
        'TIMEOUT': None,
    },
}


CACHEOPS_REDIS = env.str('REDIS_APP_URL', default='redis://redis:6379/0')

CACHEOPS = {
    'sde.*': {'ops': 'fetch', 'timeout': 86400},  # 1 day
}
