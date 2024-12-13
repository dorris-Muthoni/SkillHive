from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from django.contrib.auth.views import LoginView


class UserProfile(models.Model):
    """Extends the user model with additional details."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    skills = models.ManyToManyField('Skill', blank=True)  # Corrected 'slills' to 'skills'
    
    def __str__(self):
        return self.user.username


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name







class MyLoginView(LoginView):
    template_name = 'login.html'  

 