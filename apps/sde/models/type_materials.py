from django.db import models


class TypeMaterial(models.Model):
    id = models.IntegerField(primary_key=True)
    materials = models.JSONField()
