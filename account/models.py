from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=7, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    app_id = models.CharField(max_length=15, null=True, blank=True, unique=True)
    mat_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    place_of_birth = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=7, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    is_admitted = models.BooleanField(null=True, blank=True)
    has_accepted = models.BooleanField(null=True, blank=True, default=False)
    level = models.IntegerField(null=True, blank=True)
    year_of_admission = models.IntegerField(null=True, blank=True)
    programme_type = models.CharField(max_length=20, null=True, blank=True, default="Part Time")
    # contact address for user
    contact_address = models.TextField(null=True, blank=True)
    contact_country = models.CharField(max_length=15, null=True, blank=True)
    contact_state = models.CharField(max_length=20, null=True, blank=True)
    contact_lga = models.CharField(max_length=205, null=True, blank=True)
    #  next of kin details for the student
    kin_name = models.CharField(max_length=50, null=True, blank=True)
    kin_phone = models.CharField(max_length=15, null=True, blank=True)
    kin_relation = models.CharField(max_length=15, null=True, blank=True)
    kin_address = models.CharField(max_length=50, null=True, blank=True)

    def done_biodata(self):
        if (self.place_of_birth and
                self.date_of_birth and self.marital_status and
                self.country and self.state and self.lga and
                self.contact_lga and self.contact_state and self.contact_country and
                self.contact_address and self.kin_name and self.kin_phone and
                self.kin_address and self.kin_relation):
            return True
        else:
            return False

    def __str__(self):
        return self.app_id
