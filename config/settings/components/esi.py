from config.env import env

ESI_SSO_CLIENT_ID = env('ESI_SSO_CLIENT_ID')
ESI_SSO_CLIENT_SECRET = env('ESI_SSO_CLIENT_SECRET')
ESI_SSO_CALLBACK_URL = env('ESI_SSO_CALLBACK_URL')
ESI_USER_CONTACT_EMAIL = env('ESI_USER_CONTACT_EMAIL')
ESI_SSO_AUTHORIZATION_URL = env(
    'ESI_SSO_AUTHORIZATION_URL',
    default='https://login.eveonline.com/v2/oauth/authorize',
)
ESI_SWAGGER_URL = env(
    'ESI_SWAGGER_URL', default='https://esi.evetech.net/latest/swagger.json'
)
