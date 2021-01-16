from .models import CustomUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver


def user_receiver(sender, instance, created, **kwargs):
    if created:
        user = CustomUser.objects.get_or_create(user=instance)   

post_save.connect(user_receiver, sender=settings.AUTH_USER_MODEL)


