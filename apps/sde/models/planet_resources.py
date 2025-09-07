from django.db import models


class PlanetResource(models.Model):
    id = models.IntegerField(primary_key=True)
    power = models.IntegerField(default=None, null=True)
    workforce = models.IntegerField(default=None, null=True)
    cycle_minutes = models.IntegerField(default=None, null=True)
    harvest_silo_max = models.IntegerField(default=None, null=True)
    maturation_cycle_minutes = models.IntegerField(default=None, null=True)
    maturation_percent = models.IntegerField(default=None, null=True)
    mature_silo_max = models.IntegerField(default=None, null=True)
    reagent_harvest_amount = models.IntegerField(default=None, null=True)
    reagent_type_id = models.IntegerField(default=None, null=True)
