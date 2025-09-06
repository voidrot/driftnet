from django.db import models


class Race(models.Model):
    id = models.IntegerField(primary_key=True)
    description_id = models.JSONField(default=dict, null=True)
    icon_id = models.IntegerField(default=None, null=True)
    name_id = models.JSONField()
    ship_type_id = models.IntegerField(default=None, null=True)
    skills = models.JSONField(default=dict, null=True)

    def __str__(self):
        return f'{self.name_id["en"]}'
