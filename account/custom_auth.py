from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student


class IDBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Student.objects.get(app_id=username)
        except Student.DoesNotExist:
            return None
        else:
            if user.user.check_password(password):
                return user.user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None


class MatricBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Student.objects.get(mat_number=username)
        except Student.DoesNotExist:
            return None
        else:
            if user.user.check_password(password):
                return user.user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
