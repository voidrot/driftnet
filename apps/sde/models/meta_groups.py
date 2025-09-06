from django.db import models


class MetaGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    color = models.JSONField(default=list, null=True)
    name_id = models.JSONField()
    icon_id = models.IntegerField(default=None, null=True)
    icon_suffix = models.TextField(default=None)
    description_id = models.JSONField(default=dict, null=True)

    def __str__(self):
        return f'{self.name_id["en"]}'
