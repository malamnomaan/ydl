from django.contrib.auth.backends import BaseBackend
from webapis.models import CustomUser


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, usr_email=None, usr_password=None):
        try:
            user = CustomUser.objects.get(usr_email=usr_email)
            if user.check_password(usr_password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None