from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class customUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "height",
                    "weight",
                    "birthday",
                    "superhost",
                    "bio",
                ),
            },
        ),
    )
    list_display = (
        "username",
        "height",
        "weight",
        "birthday",
        "is_superuser",
        "is_staff",
    )
