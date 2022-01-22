from django.contrib import admin
from .models import *
from accounts.models import User
from cart.models import CartItem, Cart

# Register your models here.
admin.site.register(User)

admin.site.register(MallsList)
admin.site.register(MallsQuestion)
admin.site.register(MallsAnswer)

admin.site.register(Category)
admin.site.register(MallsItem)

admin.site.register(ProductReal)
admin.site.register(Comment)
admin.site.register(Like)

admin.site.register(Cart)
admin.site.register(CartItem)