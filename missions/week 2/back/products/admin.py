from django.contrib import admin
from .models import Product, Question


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'market', 'category')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
