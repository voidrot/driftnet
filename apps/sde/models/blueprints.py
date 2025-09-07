from django.db import models


class Blueprint(models.Model):
    id = models.IntegerField(primary_key=True)
    activities = models.JSONField()
    blueprint_type_id = models.IntegerField()
    max_production_limit = models.IntegerField()
