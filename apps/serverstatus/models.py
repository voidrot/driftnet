from django.db import models


class ServerStatus(models.Model):
    """Track server status information."""

    player_count = models.IntegerField()
    server_version = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    vip_mode = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Server Status'
        verbose_name_plural = 'Server Status'
        ordering = ['-created_at']
