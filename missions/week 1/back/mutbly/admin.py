from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'description')

admin.site.register(Question)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
