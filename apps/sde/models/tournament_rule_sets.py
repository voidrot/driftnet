from django.db import models


class TournamentRuleSet(models.Model):
    id = models.IntegerField(primary_key=True)
    banned = models.JSONField()
    maximum_pilots_match = models.IntegerField()
    maximum_points_match = models.IntegerField()
    points = models.JSONField()
    rule_set_id = models.TextField()
    rule_set_name = models.TextField()

    def __str__(self):
        return f"{self.id}"
