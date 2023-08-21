from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Provide a valid email address"))

    def create_user(self, username, firstname, lastname, email, password, **kwargs):
        if not username:
            raise ValueError(_("Username must be provided."))

        if not firstname:
            raise ValueError(_("Firstname must be provided."))

        if not lastname:
            raise ValueError(_("Lastname must be provided."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email address is required to set up account."))

        user = self.model(
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=email,
        )

        user.set_password(password)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, firstname, lastname, email, password, **kwargs
    ):

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email address is required to set up account."))

        user = self.create_user(
            username, firstname, lastname, email, password, **kwargs
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
