from django.db import models


class InvName(models.Model):
    item_id = models.IntegerField()
    item_name = models.TextField()
