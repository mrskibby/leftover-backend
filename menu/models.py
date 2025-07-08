from django.db import models
from accounts.models import RestaurantProfile

class MenuSection(models.Model):
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='menu_sections')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.restaurant.restaurant_name}"


class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.section.name}"
