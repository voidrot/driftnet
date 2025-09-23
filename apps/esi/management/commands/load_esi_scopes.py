import httpx
from django.core.management.base import BaseCommand

from apps.esi.models import Scope
from apps.sde import app_settings


class Command(BaseCommand):
    help = 'Load ESI scopes into the database'

    def handle(self, *args, **options):
        url = 'https://esi.evetech.net/latest/swagger.json'
        response = httpx.get(url, timeout=30.0)
        if response.is_success:
            data = response.json()
            scopes = (
                data.get('securityDefinitions', {}).get('evesso', {}).get('scopes', {})
            )
            scope_records = []
            for k, v in scopes.items():
                scope_records.append(
                    Scope(name=k, description=app_settings.ESI_SCOPES.get(k, v))
                )
            Scope.objects.bulk_create(
                scope_records,
                update_conflicts=True,
                unique_fields=['name'],
                update_fields=['description'],
            )
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve ESI scopes'))
        self.stdout.write(self.style.SUCCESS('Successfully loaded ESI scopes'))