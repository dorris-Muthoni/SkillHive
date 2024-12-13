from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.signals import user_logged_in

# Create or update the user profile
@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

# Award points on successful login
@receiver(user_logged_in)
def award_login_points(sender, request, user, **kwargs):
    try:
        user_profile = UserProfile.objects.get(user=user)
        user_profile.points += 10  # Award 10 points per login
        user_profile.save()
    except UserProfile.DoesNotExist:
        pass  # Handle case where user profile doesn't exist

