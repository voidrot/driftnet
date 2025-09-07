from django.db import models


class InvPosition(models.Model):
    item_id = models.IntegerField()
    pitch = models.IntegerField(default=None, null=True)
    roll = models.IntegerField(default=None, null=True)
    x = models.FloatField()
    y = models.FloatField()
    yaw = models.IntegerField(default=None, null=True)
    z = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['item_id']),
        ]
