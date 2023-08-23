from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampModel
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

User = get_user_model()


def upload_profile_photo(instance, filename):
    return f"profile/{instance.user.id}/{filename}"


class UserProfile(TimeStampModel):

    GENDER_CHOICES = Choices(
        'male', _('Male'),
        'female', _('Female')
    )

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    country = CountryField(
        verbose_name=_("Country"),
        default="GH",
        blank=False,
        null=False
    )
    street = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    house_number = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Accra",
        blank=False,
        null=False,
    )
    digital_address = models.CharField(max_length=15, null=False, blank=False)
    contact = PhoneNumberField(
        blank=True,
        region='GH'
    )
    about_me = models.TextField(
        verbose_name=_("About me"),
        default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        upload_to=upload_profile_photo
    )
    gender = models.CharField(
        max_length=10,
        verbose_name="Gender",
        choices=GENDER_CHOICES
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class UserMeasurements(TimeStampModel):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='measurements'
    )
    neck = models.DecimalField(
        verbose_name="Around neck",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    bust = models.DecimalField(
        verbose_name="Bust area",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
    arm_length = models.DecimalField(
        verbose_name="Arm length short",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    long_sleeve = models.DecimalField(
        verbose_name="Arm length long",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    bicep = models.DecimalField(
        verbose_name="Bicep",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
    wrist = models.DecimalField(
        verbose_name="Wrist",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
    torso = models.DecimalField(
        verbose_name="Torso length",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    waist = models.DecimalField(
        verbose_name="Waist",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
    hips = models.DecimalField(
        verbose_name="hips",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
    waist_to_above_knee = models.DecimalField(
        verbose_name="Skirt/ Shorts length",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    waist_to_below_knee = models.DecimalField(
        verbose_name="Trouser length",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True,
    )
    calf = models.DecimalField(
        verbose_name="Calf",
        max_digits=2,
        decimal_places=0,
        blank=True,
        null=True
    )
