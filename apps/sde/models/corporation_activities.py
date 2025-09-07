from django.db import models


class CorporationActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    name_id = models.JSONField()
