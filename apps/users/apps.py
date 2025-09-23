from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        from allauth.account.signals import user_signed_up  # noqa: PLC0415
        from django.contrib.auth.models import User  # noqa: PLC0415
        from django.dispatch import receiver  # noqa: PLC0415

        from .models import UserProfile  # noqa: PLC0415

        @receiver(user_signed_up)
        def create_user_profile(request, user, **kwargs):
            user_model = User.objects.get(pk=user.pk)
            UserProfile.objects.create(user=user_model)
