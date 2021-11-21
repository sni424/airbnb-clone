from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.StackedInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description",
                        "country", "city", "address", "price")}
        ),
        (
            "Time",
            {"fields": ("check_in", "check_out", "instant_book",)}
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths",)}
        ),
        (
            "More About the Space",
            {'classes': ('collapse',),
             "fields": ("amenity", "facility", "house_Rule",)}
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenity",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_Rule",
        "city",
        "country",
    )

    search_fields = (
        "^city", "^host__username"
    )

    filter_horizontal = (
        "amenity",
        "facility",
        "house_Rule",
    )

    def count_amenity(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"Photo Admin Definition"""

    list_display = (
        "__str__", "get_thumnail",
    )

    def get_thumnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumnail.short_description = "Thumnail"
