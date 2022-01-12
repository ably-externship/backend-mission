from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Seller,SellerAdmin)

