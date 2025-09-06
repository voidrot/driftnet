from django.db import models


class DogmaEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    disallow_auto_repeat = models.BooleanField()
    discharge_attribute_id = models.IntegerField(default=None, null=True)
    duration_attribute_id = models.IntegerField(default=None, null=True)
    effect_category = models.IntegerField()
    effect_id = models.IntegerField()
    effect_name = models.TextField()
    electronic_chance = models.BooleanField()
    guid = models.TextField(default=None)
    is_assistance = models.BooleanField()
    is_offensive = models.BooleanField()
    is_warp_safe = models.BooleanField()
    propulsion_chance = models.BooleanField()
    published = models.BooleanField()
    range_chance = models.BooleanField()
    distribution = models.IntegerField(default=None, null=True)
    falloff_attribute_id = models.IntegerField(default=None, null=True)
    range_attribute_id = models.IntegerField(default=None, null=True)
    tracking_speed_attribute_id = models.IntegerField(default=None, null=True)
    description_id = models.JSONField(default=dict, null=True)
    display_name_id = models.JSONField(default=dict, null=True)
    icon_id = models.IntegerField(default=None, null=True)
    modifier_info = models.JSONField(default=list, null=True)
    sfx_name = models.TextField(default=None)
    npc_usage_chance_attribute_id = models.IntegerField(default=None, null=True)
    npc_activation_chance_attribute_id = models.IntegerField(default=None, null=True)
    fitting_usage_chance_attribute_id = models.IntegerField(default=None, null=True)
    resistance_attribute_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f'{self.id}'
