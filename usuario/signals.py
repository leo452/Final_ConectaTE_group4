
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from usuario import models

@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.is_staff=True
        instance.save()