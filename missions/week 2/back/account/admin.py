from django.contrib import admin
from account.models import User
from product.models import Product, Productreal


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    pass


@admin.register(Productreal)
class Product_option_admin(admin.ModelAdmin):
    pass

