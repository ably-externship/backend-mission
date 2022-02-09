from django.contrib import admin

from .models import Product, Product_option


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price')

admin.site.register(Product, ProductAdmin)


class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'opt1_type', 'opt1_name', 'opt1_price')

admin.site.register(Product_option, ProductOptionAdmin)