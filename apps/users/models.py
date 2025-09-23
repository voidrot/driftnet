from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile of {self.user.username}'
