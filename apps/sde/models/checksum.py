from django.db import models


# Create your models here.
class Checksum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    checksum = models.CharField(max_length=32)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
