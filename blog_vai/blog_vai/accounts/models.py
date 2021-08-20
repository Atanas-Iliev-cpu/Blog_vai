from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from blog_vai.accounts.managers import SiteUserManager
from .validators import first_letter_is_capital_validator, phone_number_validator_for_length, is_digits_phone_validator


class SiteUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = SiteUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        SiteUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[first_letter_is_capital_validator]
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[first_letter_is_capital_validator]
    )
    email = models.EmailField(
        # unique=True,
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            phone_number_validator_for_length,
            is_digits_phone_validator,
        ],
    )


from .signals import *
