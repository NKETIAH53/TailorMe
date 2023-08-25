from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE_CHOICES = Choices("tailor", _("Tailor"), "client", _("Client"))
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    firstname = models.CharField(
        verbose_name=_("Firstname"),
        max_length=255,
    )
    lastname = models.CharField(
        verbose_name=_("Lastname"),
        max_length=255,
    )
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "firstname", "lastname"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def get_full_name(self):
        return f"{self.firstname.title()} {self.lastname.title()}"

    @property
    def get_short_name(self):
        return f"{self.username}"
