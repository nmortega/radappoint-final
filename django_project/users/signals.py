from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is saved, send the signal (the signal to be received by @receiver)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): # The receiver is this create_profile function
    if created:
        Profile.objects.create(user=instance) # If the user is created then create a profile object with the user equal to the instance of the user that was created

@receiver(post_save, sender=User)
def save(sender, instance, **kwargs): # kwargs just accepts any additional keyword argument at end of function
    instance.profile.save()