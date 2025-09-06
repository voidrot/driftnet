from django.db import models


class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    mass = models.FloatField(default=None, null=True)
    name = models.JSONField()
    portion_size = models.IntegerField()
    published = models.BooleanField()
    volume = models.FloatField(default=None, null=True)
    radius = models.FloatField(default=None, null=True)
    description = models.JSONField(default=dict, null=True)
    graphic_id = models.IntegerField(default=None, null=True)
    sound_id = models.IntegerField(default=None, null=True)
    icon_id = models.IntegerField(default=None, null=True)
    race_id = models.IntegerField(default=None, null=True)
    sof_faction_name = models.TextField(default=None)
    base_price = models.FloatField(default=None, null=True)
    market_group_id = models.IntegerField(default=None, null=True)
    capacity = models.FloatField(default=None, null=True)
    meta_group_id = models.IntegerField(default=None, null=True)
    variation_parent_type_id = models.IntegerField(default=None, null=True)
    faction_id = models.IntegerField(default=None, null=True)
    masteries = models.JSONField(default=dict, null=True)
    traits = models.JSONField(default=dict, null=True)
    sof_material_set_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f"{self.id}"
