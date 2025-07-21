from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Customer, RestaurantProfile

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # Optional: Customize the user display in admin
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("dob", "address")}),
    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "address"]

@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "restaurant_name", "phone_number"]
