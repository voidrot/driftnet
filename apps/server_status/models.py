from django.db import models


class ServerStatus(models.Model):
    """track server status information."""

    player_count = models.IntegerField()
    server_version = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    vip_mode = models.BooleanField(null=True, default=False)
