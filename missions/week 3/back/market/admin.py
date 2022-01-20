from django.contrib import admin

from .models import Market


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'admin', 'url', 'email')

admin.site.register(Market, MarketAdmin)