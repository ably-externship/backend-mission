from django.contrib import admin

from .models import Cart
from .models import CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
