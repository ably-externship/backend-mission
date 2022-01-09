from django.contrib import admin

# Register your models here.
from .models import Product, Question

admin.site.register(Product)
admin.site.register(Question)