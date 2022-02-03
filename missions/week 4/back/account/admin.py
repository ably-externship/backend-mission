from django.contrib import admin
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']


# @admin.register(Seller)
# class SellerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'seller', 'is_staff']
