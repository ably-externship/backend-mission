from django.contrib import admin
from . import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    field = "color"
    ordering = ["color"]


@admin.register(models.size_upper, models.size_outer, models.size_onepiece)
class SizeAdmin(admin.ModelAdmin):
    field = "size"
    ordering = ["size"]
