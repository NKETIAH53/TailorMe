from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "id",
        "email",
        "username",
        "firstname",
        "lastname",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email", "username"]
    list_filter = [
        "email",
        "username",
        "firstname",
        "lastname",
        "is_staff",
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "firstname",
                    "lastname",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ["email", "username", "firstname", "lastname"]

admin.site.register(User, UserAdmin)
