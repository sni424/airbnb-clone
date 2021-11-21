from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models
# Register your models here.


class RoomInline(admin.StackedInline):

    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets+(("Custom User", {"fields": (
        "Avatar", "Gender", "Bio", "Birthdate", "Language", "currency", "superhost",)}),)

    list_filter = UserAdmin.list_filter + (
        "superhost",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "Language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
