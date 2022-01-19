from django.contrib import admin
from .models import Product, Question, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'market', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
