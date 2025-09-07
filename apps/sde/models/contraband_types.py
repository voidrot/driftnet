from django.db import models


class ContrabandType(models.Model):
    id = models.IntegerField(primary_key=True)
    factions = models.JSONField()
