from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(bool, False),
    REDIS_URL=(str, 'redis://localhost:6379/0'),
    REDIS_SSL=(bool, False),
    # App Logging level
    APPS_ESI_LOG_LEVEL=(str, 'INFO'),
    APPS_USERS_LOG_LEVEL=(str, 'INFO'),
    APPS_SDE_LOG_LEVEL=(str, 'INFO'),
    APPS_ESI_UTILS_LOG_LEVEL=(str, 'INFO'),
    APPS_DASHBOARD_LOG_LEVEL=(str, 'INFO'),
    APPS_ALLIANCE_LOG_LEVEL=(str, 'INFO'),
    APPS_ASSET_LOG_LEVEL=(str, 'INFO'),
    APPS_CHARACTER_LOG_LEVEL=(str, 'INFO'),
    APPS_CLONES_LOG_LEVEL=(str, 'INFO'),
    APPS_CONTACTS_LOG_LEVEL=(str, 'INFO'),
    APPS_CONTRACTS_LOG_LEVEL=(str, 'INFO'),
    APPS_CORPORATIONS_LOG_LEVEL=(str, 'INFO'),
    APPS_FACTION_WARFARE_LOG_LEVEL=(str, 'INFO'),
    APPS_FITTINGS_LOG_LEVEL=(str, 'INFO'),
    APPS_FLEETS_LOG_LEVEL=(str, 'INFO'),
    APPS_INCURSIONS_LOG_LEVEL=(str, 'INFO'),
    APPS_INDUSTRY_LOG_LEVEL=(str, 'INFO'),
    APPS_INSURANCE_LOG_LEVEL=(str, 'INFO'),
    APPS_KILLMAILS_LOG_LEVEL=(str, 'INFO'),
    APPS_LOCATION_LOG_LEVEL=(str, 'INFO'),
    APPS_LOYALTY_LOG_LEVEL=(str, 'INFO'),
    APPS_MAIL_LOG_LEVEL=(str, 'INFO'),
    APPS_MARKET_LOG_LEVEL=(str, 'INFO'),
    APPS_PLANETARY_INTERACTION_LOG_LEVEL=(str, 'INFO'),
    APPS_SKILLS_LOG_LEVEL=(str, 'INFO'),
    APPS_SOVEREIGNTY_LOG_LEVEL=(str, 'INFO'),
    APPS_WALLET_LOG_LEVEL=(str, 'INFO'),
    APPS_WARS_LOG_LEVEL=(str, 'INFO'),
)

BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR / 'apps'

if Path(BASE_DIR / '.env').exists():
    environ.Env.read_env(Path(BASE_DIR / '.env'))
