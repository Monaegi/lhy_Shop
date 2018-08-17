from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class SettingsBackend:
    def authenticate(self, request, username=None, password=None):
        username_valid = check_password(username, settings.ADMIN_USERNAME)
        password_valid = check_password(password, settings.ADMIN_PASSWORD)
        if username_valid and password_valid:
            user, __ = User.objects.get_or_create(
                username=username,
                defaults={
                    'is_staff': True,
                    'is_superuser': True,
                }
            )
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
