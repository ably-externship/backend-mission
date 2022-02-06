from django.contrib import admin

# Register your models here.
from products.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(ProductImage)
