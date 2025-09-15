# Create your models here.
from django.db import models


class War(models.Model):
    declared = models.DateTimeField()
    started = models.DateTimeField(null=True)
    finished = models.DateTimeField(null=True)
    mutual = models.BooleanField()
    open_for_allies = models.BooleanField()
    retracted = models.DateTimeField(null=True)
    aggressor = models.JSONField()
    allies = models.JSONField()
    defender = models.JSONField()
    # TODO: Add a one-to-many relationship to killmails
