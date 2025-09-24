from django.db import models
import logging

logger = logging.getLogger(__name__)

class TokenQuerySet(models.QuerySet):
    pass

class TokenManager(models.Manager):
    pass
