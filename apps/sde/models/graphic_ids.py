from django.db import models


class GraphicId(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(default=None)
    graphic_file = models.TextField(default=None)
    icon_info = models.JSONField(default=dict, null=True)
    sof_faction_name = models.TextField(default=None)
    sof_hull_name = models.TextField(default=None)
    sof_race_name = models.TextField(default=None)
    sof_layout = models.JSONField(default=list, null=True)
