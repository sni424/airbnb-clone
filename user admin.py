from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets+(("Custom User", {"fields": (
        "Avatar", "Gender", "Bio", "Birthdate", "Language", "currency", "Superhost",)}),)

    list_filter = UserAdmin.list_filter + (
        "Superhost",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "Language",
        "currency",
        "Superhost",
        "is_staff",
        "is_superuser",
    )
