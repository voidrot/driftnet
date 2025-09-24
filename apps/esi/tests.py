from apps.esi import app_settings
from apps.esi import client


class TestESIClientHelpers:
    def test_get_user_agent(self) -> None:
        ua = client._get_user_agent()
        assert app_settings.ESI_CONTACT_EMAIL in ua
        assert app_settings.ESI_APP_NAME in ua
        assert app_settings.ESI_APP_VERSION in ua
        if app_settings.ESI_APP_URL:
            assert app_settings.ESI_APP_URL in ua
            assert (
                ua
                == f'{app_settings.ESI_APP_NAME}/{app_settings.ESI_APP_VERSION} {app_settings.ESI_CONTACT_EMAIL} (+{app_settings.ESI_APP_URL})'
            )
        else:
            assert (
                ua
                == f'{app_settings.ESI_APP_NAME}/{app_settings.ESI_APP_VERSION} {app_settings.ESI_CONTACT_EMAIL}'
            )
