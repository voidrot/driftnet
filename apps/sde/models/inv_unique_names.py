from django.db import models


class InvUniqueName(models.Model):
    group_id = models.IntegerField()
    item_id = models.IntegerField()
    item_name = models.TextField()
