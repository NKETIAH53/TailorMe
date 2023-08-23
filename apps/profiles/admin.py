from django.contrib import admin
from .models import UserProfile, UserMeasurements


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user'
    ]


admin.site.register(UserProfile, ProfileAdmin)


class MeasurementsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'profile'
    ]


admin.site.register(UserMeasurements, MeasurementsAdmin)
