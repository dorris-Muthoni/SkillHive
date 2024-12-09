from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.views import LoginView


class UserProfile(models.Model):
    """Extends the user model with additional details."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    """Represents skills a user can share or learn."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class MyLoginView(LoginView):
    template_name = 'login.html'  