from django.contrib import admin
from .models import Product, Category, Brand, Comment, Image, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Cart)


class ImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Product, ProductAdmin)


class CategoryInline(admin.TabularInline):
    model = Category


