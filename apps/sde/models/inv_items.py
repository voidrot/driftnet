from django.db import models


class InvItem(models.Model):
    flag_id = models.IntegerField()
    item_id = models.IntegerField(primary_key=True)
    location_id = models.IntegerField()
    owner_id = models.IntegerField()
    quantity = models.IntegerField()
    type_id = models.IntegerField()
