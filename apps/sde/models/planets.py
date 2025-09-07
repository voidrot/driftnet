from django.db import models


class Planet(models.Model):
    id = models.IntegerField(primary_key=True)
    celestial_index = models.IntegerField()
    planet_attributes = models.JSONField()
    position = models.JSONField()
    radius = models.IntegerField()
    statistics = models.JSONField()
    type_id = models.IntegerField()
    npc_stations = models.JSONField(default=dict, null=True)
    planet_name_id = models.IntegerField(default=None, null=True)
