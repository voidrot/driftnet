from django.db import models


class Constellation(models.Model):
    id = models.IntegerField(primary_key=True)
    center = models.JSONField()
    constellation_id = models.IntegerField()
    max = models.JSONField()
    min = models.JSONField()
    name_id = models.IntegerField()
    radius = models.FloatField()
    faction_id = models.IntegerField(default=None, null=True)
    wormhole_class_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f'{self.name_id["en"]}'
