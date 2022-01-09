from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Market)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(ProductImage)
admin.site.register(ProductQuestion)
