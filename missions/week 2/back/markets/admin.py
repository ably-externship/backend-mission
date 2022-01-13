from django.contrib import admin
from .models import Market


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass
