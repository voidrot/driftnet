from environs import env

ESI_CONTACT_EMAIL = env.str('ESI_CONTACT_EMAIL', default='bbrady145@gmail.com')
ESI_APP_URL = env.str('ESI_APP_URL', default='https://github.com/voidrot/voidlink')
ESI_APP_VERSION = env.str('ESI_APP_VERSION', default='development')
ESI_SSO_CALLBACK_URL = env.str('ESI_SSO_CALLBACK_URL')

ESI_SSO_CLIENT_ID = env('ESI_SSO_CLIENT_ID')
ESI_SSO_CLIENT_SECRET = env('ESI_SSO_CLIENT_SECRET')
