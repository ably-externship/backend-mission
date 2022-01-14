from django.contrib import admin
from .models import Product
from .models import Product_options

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )

admin.site.register(Product,ProductAdmin)

class Product_optionAdmin(admin.ModelAdmin):
    list_display = ('opt1_type', 'opt1_name', 'opt1_price', 'opt1_stock')

admin.site.register(Product_options,Product_optionAdmin)