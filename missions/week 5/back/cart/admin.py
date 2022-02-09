from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Cart, CartAdmin)
