from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    ROLES = Choices("tailor", _("Tailor"), "client", _("Client"))
    fullname = serializers.CharField(source="get_full_name", read_only=True)
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=ROLES, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "firstname",
            "lastname",
            "username",
            "fullname",
            "email",
            "role",
        ]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "This username already exists, please use a different one."
            )
        return value
