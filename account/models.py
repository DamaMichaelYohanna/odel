from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    middle_name = models.TextField(null=True, blank=True)
    phone = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    app_id = models.TextField(null=True, blank=True, unique=True)
    mat_number = models.TextField(null=True, blank=True, unique=True)
    place_of_birth = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    lga = models.TextField(null=True, blank=True)
    home_town = models.TextField(null=True, blank=True)
    # contact address for user
    contact_address = models.TextField(null=True, blank=True)
    contact_country = models.TextField(null=True, blank=True)
    contact_state = models.TextField(null=True, blank=True)
    contact_lga = models.TextField(null=True, blank=True)
    #  next of kin details for the student
    name = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    relation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.app_id