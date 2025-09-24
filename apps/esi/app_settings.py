from django.conf import settings

ESI_CONTACT_EMAIL = getattr(settings, 'ESI_CONTACT_EMAIL', None)
"""Contact email for CCP to contact in case of issues with the application."""

ESI_APP_URL = getattr(settings, 'ESI_APP_URL', None)
"""URL for the application."""

ESI_APP_NAME = getattr(settings, 'ESI_APP_NAME', 'Voidlink')
"""Name of the application accessing the ESI API."""

ESI_APP_VERSION = getattr(settings, 'ESI_APP_VERSION', None)
"""Version of the application accessing the ESI API."""

ESI_CLIENT_TENANT = getattr(settings, 'ESI_CLIENT_TENANT', 'tranquility')
"""ESI client tenant, usually 'tranquility'."""

ESI_COMPATIBILITY_DATE = getattr(settings, 'ESI_COMPATIBILITY_DATE', '2025-08-26')
"""ESI compatibility date, in YYYY-MM-DD format."""

ESI_CACHE_BACKEND_NAME = getattr(settings, 'ESI_CACHE_BACKEND_NAME', 'esi')
"""Cache backend name for ESI caching."""

ESI_OAUTH_URL = getattr(
    settings, 'ESI_SSO_BASE_URL', 'https://login.eveonline.com/v2/oauth'
)
"""Base URL for EVE Online SSO OAuth2."""

ESI_OAUTH_LOGIN_URL = getattr(
    settings, 'ESI_SSO_LOGIN_URL', ESI_OAUTH_URL + '/authorize/'
)
"""Login URL for EVE Online SSO OAuth2."""

ESI_TOKEN_URL = getattr(settings, 'ESI_CODE_EXCHANGE_URL', ESI_OAUTH_URL + '/token')
"""The URL to redirect users to for EVE SSO login."""

ESI_OPENAPI_URL = getattr(
    settings, 'ESI_OPENAPI_URL', 'https://esi.evetech.net/meta/openapi.json'
)
"""The URL to the ESI OpenAPI specification."""

ESI_API_URL = getattr(settings, 'ESI_API_URL', 'https://esi.evetech.net/')
"""The base URL for the ESI API."""

ESI_SPEC_CACHE_DURATION = int(getattr(settings, 'ESI_SPEC_CACHE_DURATION', 3600))
"""The duration, in seconds, to cache the ESI OpenAPI specification."""

ESI_CLIENT_CONNECT_TIMEOUT = getattr(settings, 'ESI_CLIENT_CONNECT_TIMEOUT', 5.0)
"""Default connect timeout settings for the HTTPX client used to interact with the ESI API."""

ESI_CLIENT_READ_TIMEOUT = getattr(settings, 'ESI_CLIENT_READ_TIMEOUT', 10.0)
"""Default read timeout settings for the HTTPX client used to interact with the ESI API."""

ESI_CLIENT_WRITE_TIMEOUT = getattr(settings, 'ESI_CLIENT_WRITE_TIMEOUT', 10.0)
"""Default write timeout settings for the HTTPX client used to interact with the ESI API."""

ESI_CLIENT_POOL_TIMEOUT = getattr(settings, 'ESI_CLIENT_POOL_TIMEOUT', 5.0)
"""Default pool timeout settings for the HTTPX client used to interact with the ESI API."""

ESI_CONNECTION_ERROR_MAX_RETRIES = getattr(
    settings, 'ESI_CONNECTION_ERROR_MAX_RETRIES', 3
)
"""Max retries on failed connections."""

ESI_SERVER_ERROR_MAX_RETRIES = getattr(settings, 'ESI_SERVER_ERROR_MAX_RETRIES', 3)
"""Max retries on server errors."""

ESI_SERVER_ERROR_BACKOFF_FACTOR = getattr(
    settings, 'ESI_SERVER_ERROR_BACKOFF_FACTOR', 0.2
)
"""Backoff factor for retries on server error."""

ESI_CONNECTION_POOL_MAXSIZE = getattr(settings, 'ESI_CONNECTION_POOL_MAXSIZE', 10)
"""Max size of the connection pool.

Increase this setting if you hav more parallel
threads connected to ESI at the same time.
"""

ESI_TOKEN_VALID_DURATION = getattr(settings, 'ESI_TOKEN_VALID_DURATION', 1170)
"""The duration, in seconds, that an ESI token is considered valid."""

ESI_TOKEN_VERIFY_URL = getattr(
    settings, 'ESI_TOKEN_EXCHANGE_URL', ESI_OAUTH_URL + '/verify'
)
"""The URL to verify ESI tokens."""

ESI_TOKEN_JWT_AUDIENCE = str(getattr(settings, 'ESI_TOKEN_JWT_AUDIENCE', 'EVE Online'))
"""The audience to use when validating JWT tokens."""

ESI_TOKEN_JWK_SET_URL = 'https://login.eveonline.com/oauth/jwks'  # noqa: S105
"""The URL to fetch the JWK set for validating JWT tokens."""

ESI_JWKS_METADATA_URL = (
    'https://login.eveonline.com/.well-known/oauth-authorization-server'
)
"""The URL to fetch the JWK set metadata for validating JWT tokens."""

ESI_JWKS_ACCEPTED_ISSUERS = ('logineveonline.com', 'https://login.eveonline.com')
"""The accepted issuers to use when validating JWT tokens."""

ESI_JWKS_METADATA_CACHE_TIME = 300
"""The duration, in seconds, to cache the JWK set metadata."""

ESI_CACHE_RESPONSE = getattr(settings, 'ESI_CACHE_RESPONSE', True)
"""Disable to stop caching endpoint responses."""

ESI_SCOPES = {
    'publicData': 'Allows reading public data',
    'esi-calendar.respond_calendar_events.v1': 'Allows responding to calendar events',
    'esi-calendar.read_calendar_events.v1': 'Allows reading calendar events',
    'esi-location.read_location.v1': 'Allows reading location data',
    'esi-location.read_ship_type.v1': 'Allows reading ship type data',
    'esi-mail.organize_mail.v1': 'Allows organizing mail',
    'esi-mail.read_mail.v1': 'Allows reading mail',
    'esi-mail.send_mail.v1': 'Allows sending mail',
    'esi-skills.read_skills.v1': 'Allows reading skills',
    'esi-skills.read_skillqueue.v1': 'Allows reading skill queue',
    'esi-wallet.read_character_wallet.v1': 'Allows reading character wallet',
    'esi-wallet.read_corporation_wallet.v1': 'Allows reading corporation wallet',
    'esi-search.search_structures.v1': 'Allows searching structures',
    'esi-clones.read_clones.v1': 'Allows reading clones',
    'esi-characters.read_contacts.v1': 'Allows reading contacts',
    'esi-universe.read_structures.v1': 'Allows reading structures',
    'esi-killmails.read_killmails.v1': 'Allows reading killmails',
    'esi-corporations.read_corporation_membership.v1': 'Allows reading corporation membership',
    'esi-assets.read_assets.v1': 'Allows reading assets',
    'esi-planets.manage_planets.v1': 'Allows managing planets',
    'esi-fleets.read_fleet.v1': 'Allows reading fleet information',
    'esi-fleets.write_fleet.v1': 'Allows writing fleet information',
    'esi-ui.open_window.v1': 'Allows opening a UI window',
    'esi-ui.write_waypoint.v1': 'Allows writing a waypoint',
    'esi-characters.write_contacts.v1': 'Allows writing contacts',
    'esi-fittings.read_fittings.v1': 'Allows reading fittings',
    'esi-fittings.write_fittings.v1': 'Allows writing fittings',
    'esi-markets.structure_markets.v1': 'Allows accessing structure markets',
    'esi-corporations.read_structures.v1': 'Allows reading corporation structures',
    'esi-characters.read_loyalty.v1': 'Allows reading loyalty points',
    'esi-characters.read_chat_channels.v1': 'Allows reading chat channels',
    'esi-characters.read_medals.v1': 'Allows reading medals',
    'esi-characters.read_standings.v1': 'Allows reading standings',
    'esi-characters.read_agents_research.v1': 'Allows reading agents research',
    'esi-characters.read_implants.v1': 'Allows reading implants',
    'esi-industry.read_character_jobs.v1': 'Allows reading character jobs',
    'esi-markets.read_character_orders.v1': 'Allows reading character orders',
    'esi-characters.read_blueprints.v1': 'Allows reading blueprints',
    'esi-characters.read_corporation_roles.v1': 'Allows reading corporation roles',
    'esi-location.read_online.v1': 'Allows reading online status',
    'esi-contracts.read_character_contracts.v1': 'Allows reading character contracts',
    'esi-clones.read_implants.v1': 'Allows reading implants',
    'esi-characters.read_fatigue.v1': 'Allows reading fatigue',
    'esi-killmails.read_corporation_killmails.v1': 'Allows reading corporation killmails',
    'esi-corporations.track_members.v1': 'Allows tracking corporation members',
    'esi-wallet.read_corporation_wallets.v1': 'Allows reading corporation wallets',
    'esi-characters.read_notifications.v1': 'Allows reading notifications',
    'esi-corporations.read_divisions.v1': 'Allows reading corporation divisions',
    'esi-corporations.read_contacts.v1': 'Allows reading corporation contacts',
    'esi-assets.read_corporation_assets.v1': 'Allows reading corporation assets',
    'esi-corporations.read_titles.v1': 'Allows reading corporation titles',
    'esi-corporations.read_blueprints.v1': 'Allows reading corporation blueprints',
    'esi-contracts.read_corporation_contracts.v1': 'Allows reading corporation contracts',
    'esi-corporations.read_standings.v1': 'Allows reading corporation standings',
    'esi-corporations.read_starbases.v1': 'Allows reading corporation starbases',
    'esi-industry.read_corporation_jobs.v1': 'Allows reading corporation jobs',
    'esi-markets.read_corporation_orders.v1': 'Allows reading corporation orders',
    'esi-corporations.read_container_logs.v1': 'Allows reading corporation container logs',
    'esi-industry.read_character_mining.v1': 'Allows reading character mining',
    'esi-industry.read_corporation_mining.v1': 'Allows reading corporation mining',
    'esi-planets.read_customs_offices.v1': 'Allows reading customs offices',
    'esi-characters.read_customs_offices.v1': 'Allows reading customs offices',
    'esi-corporations.read_facilities.v1': 'Allows reading corporation facilities',
    'esi-corporations.read_medals.v1': 'Allows reading corporation medals',
    'esi-characters.read_titles.v1': 'Allows reading character titles',
    'esi-alliances.read_contacts.v1': 'Allows reading alliance contacts',
    'esi-characters.read_fw_stats.v1': 'Allows reading character FW stats',
    'esi-corporations.read_fw_stats.v1': 'Allows reading corporation FW stats',
    'esi-corporations.read_projects.v1': 'Allows reading corporation projects',
}
