from django.contrib import admin
from .models import MarketDailySales,ProductDailySales
# Register your models here.

admin.site.register(MarketDailySales)
admin.site.register(ProductDailySales)