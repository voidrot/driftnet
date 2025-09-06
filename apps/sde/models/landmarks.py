from django.db import models


class Landmark(models.Model):
    id = models.IntegerField(primary_key=True)
    description_id = models.IntegerField()
    landmark_name_id = models.IntegerField()
    position = models.JSONField()
    icon_id = models.IntegerField(default=None, null=True)
    location_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f'{self.id}'
