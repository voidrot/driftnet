from django.db import models


class ControlTowerResource(models.Model):
    id = models.IntegerField(primary_key=True)
    resources = models.JSONField()
