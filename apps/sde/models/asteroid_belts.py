from django.db import models


class AsteroidBelt(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.JSONField()
    statistics = models.JSONField(default=dict, null=True)
    type_id = models.IntegerField()
    asteroid_belt_name_id = models.IntegerField(default=None, null=True)
