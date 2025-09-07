from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(bool, False),
    REDIS_URL=(str, 'redis://localhost:6379/0'),
    REDIS_SSL=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR / 'apps'

if Path(BASE_DIR / '.env').exists():
    environ.Env.read_env(Path(BASE_DIR / '.env'))
