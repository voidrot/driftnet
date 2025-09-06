from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    center = models.JSONField()
    description_id = models.IntegerField(default=None, null=True)
    faction_id = models.IntegerField(default=None, null=True)
    max = models.JSONField()
    min = models.JSONField()
    name_id = models.IntegerField()
    nebula = models.IntegerField()
    region_id = models.IntegerField()
    wormhole_class_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f'{self.name_id["en"]}'
