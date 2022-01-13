from django.contrib import admin
from .models import Product, Question


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'market', 'price', 'color', 'size', 'category', 'stock')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
