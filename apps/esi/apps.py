from django.apps import AppConfig


class EsiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.esi'

    def ready(self) -> None:
        super().ready()
        from apps.esi import checks  # noqa
