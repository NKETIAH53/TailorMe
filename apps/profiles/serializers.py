from django.utils.translation import gettext_lazy as _
from django_countries.serializers import CountryFieldMixin
from model_utils import Choices
from rest_framework import serializers

from apps.users.serializers import UserSerializer

from .models import UserProfile


class UserProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    GENDER = Choices("male", _("Male"), "female", _("Female"))

    gender = serializers.ChoiceField(choices=GENDER, required=False)
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "gender",
            "street",
            "house_number",
            "region",
            "city",
            "digital_address",
            "contact",
            "about_me",
        ]
