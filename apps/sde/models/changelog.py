from django.db import models

class Changelog(models.Model):
    """
    Model to store change logs for tracking changes in the system.
    """
    build_number = models.IntegerField(primary_key=True)
    change_date = models.DateField()
    file_changes = models.JSONField(default=dict)
    field_changes = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-build_number']
        verbose_name = "Changelog"
        verbose_name_plural = "Changelogs"

    def __str__(self):
        return f"{self.build_number} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
