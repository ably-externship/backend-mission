from django.contrib import admin
from .models import *

class ProductInventoryInline(admin.TabularInline):
    model = Inventory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInventoryInline]
    prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Market)
admin.site.register(Product, ProductAdmin)
admin.site.register(DetailImage)
admin.site.register(Inventory)
admin.site.register(Question)
