from django.db import models


class Skin(models.Model):
    id = models.IntegerField(primary_key=True)
    allow_ccpdevs = models.BooleanField()
    internal_name = models.TextField()
    skin_id = models.IntegerField()
    skin_material_id = models.IntegerField()
    types = models.JSONField()
    visible_serenity = models.BooleanField()
    visible_tranquility = models.BooleanField()
    is_structure_skin = models.BooleanField(default=False, null=True)
    skin_description = models.TextField(default=None)
