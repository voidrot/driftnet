from django.db import models


class MarketGroupWithTypes(models.Model):
    market_group_id = models.IntegerField(primary_key=True)
    market_group_name = models.CharField(max_length=255)
    parent_group_id = models.IntegerField(null=True)
    type_id = models.IntegerField(null=True)
    type_name = models.CharField(max_length=255, null=True)

    class Meta:
        managed = False
        db_table = 'market_group_with_types'
