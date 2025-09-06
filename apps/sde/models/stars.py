from django.db import models


class Star(models.Model):
    id = models.IntegerField()
    radius = models.IntegerField()
    statistics = models.JSONField()
    type_id = models.IntegerField()

    def __str__(self):
        return f'{self.id}'
