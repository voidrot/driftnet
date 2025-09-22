from environs import env
from split_settings.tools import include
from split_settings.tools import optional

env.read_env()

ENV = env.str('DJANGO_ENV', 'development')

base_settings = [
    'components/*.py',
    'environments/{}.py'.format(ENV),  # noqa: UP032
    optional('environments/local.py'),
]


include(*base_settings)
