from django.contrib import admin
from .models import Product, ProductCategory,Question,Answer, RealProduct
# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(RealProduct)
admin.site.register(Question)

admin.site.register(Answer)