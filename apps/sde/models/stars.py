from django.db import models


class Star(models.Model):
    id = models.IntegerField(primary_key=True)
    radius = models.IntegerField()
    statistics = models.JSONField()
    type_id = models.IntegerField()
