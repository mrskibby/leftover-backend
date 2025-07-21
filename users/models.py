from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
class RestaurantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.restaurant_name

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Customer: {self.user.username}"
