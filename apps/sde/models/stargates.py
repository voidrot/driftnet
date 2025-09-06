from django.db import models


class Stargate(models.Model):
    id = models.IntegerField(primary_key=True)
    destination = models.IntegerField()
    position = models.JSONField()
    type_id = models.IntegerField()

    def __str__(self):
        return f'{self.id}'
