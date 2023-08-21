from django.contrib import admin
from .models import CommonProfileFields, UserProfile, UserMeasurements

admin.site.register(UserProfile)
admin.site.register(UserMeasurements)
