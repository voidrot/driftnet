from django.db import models


class InvName(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.TextField()
