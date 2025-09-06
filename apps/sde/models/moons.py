from django.db import models


class Moon(models.Model):
    id = models.IntegerField(primary_key=True)
    planet_attributes = models.JSONField()
    position = models.JSONField()
    radius = models.IntegerField()
    statistics = models.JSONField(default=dict, null=True)
    type_id = models.IntegerField()
    npc_stations = models.JSONField(default=dict, null=True)
    moon_name_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f'{self.id}'
