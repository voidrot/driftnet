import logging

from django.conf import settings
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

logger = logging.getLogger(__name__)


class Scope(models.Model):
    """A scope defines the access permissions for an ESI token.

    Attributes:
        name (str): The name of the scope.
        description (str): A brief description of what the scope allows.
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Scope'
        verbose_name_plural = 'Scopes'
        ordering = ['name']

    def __str__(self):
        return self.name


class Token(ExportModelOperationsMixin(models.Model)):
    """An ESI token representing a user's authentication and authorization.

    Attributes:
        access_token (str): The access token string.
        refresh_token (str): The refresh token string.
        expires_at (datetime): The expiration time of the access token.
        character_id (int): The ID of the character associated with the token.
        character_name (str): The name of the character associated with the token.
        scopes (ManyToMany[Scope]): The scopes associated with this token.
        created_at (datetime): The timestamp when the token was created.
        updated_at (datetime): The timestamp when the token was last updated.
    """

    TOKEN_TYPE_CHOICES = [
        ('character', 'Character'),
        ('corporation', 'Corporation'),
    ]

    character_id = models.BigIntegerField(db_index=True)
    character_name = models.CharField(max_length=100, db_index=True)
    token_type = models.CharField(
        max_length=50, choices=TOKEN_TYPE_CHOICES, db_index=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, editable=False)
    refresh_token = models.CharField(max_length=255, editable=False)
    character_owner_hash = models.CharField(max_length=255, db_index=True)
    scopes = models.ManyToManyField(Scope)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ['-created_at']

    def __str__(self):
        return f'Token for {self.character_name} ({self.character_id})'
