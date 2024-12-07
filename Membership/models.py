
from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    """Represents membership tiers."""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    benefits = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """Tracks user payments and transactions."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Transaction {self.id} - {self.user.username}"

