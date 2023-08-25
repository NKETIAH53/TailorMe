import logging
from django.db.models.signals import post_save
from tailor_me.settings import AUTH_USER_MODEL
from django.dispatch import receiver
from .models import UserProfile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
