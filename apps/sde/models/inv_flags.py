from django.db import models


class InvFlag(models.Model):
    flag_id = models.IntegerField()
    flag_name = models.TextField()
    flag_text = models.TextField()
    order_id = models.IntegerField()
