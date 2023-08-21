# Generated by Django 4.2.4 on 2023-08-21 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="usermeasurements",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="profiles.userprofile"
            ),
        ),
    ]