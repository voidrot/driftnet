from django.db import models


class SovereigntyUpgrade(models.Model):
    id = models.IntegerField(primary_key=True)
    fuel_hourly_upkeep = models.IntegerField(default=None, null=True)
    fuel_startup_cost = models.IntegerField(default=None, null=True)
    fuel_type_id = models.IntegerField(default=None, null=True)
    mutually_exclusive_group = models.TextField()
    power_allocation = models.IntegerField()
    workforce_allocation = models.IntegerField()
