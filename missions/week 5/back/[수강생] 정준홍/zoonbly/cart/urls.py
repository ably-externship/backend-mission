from django import views
from django.urls import path
from .views import *

app_name = "cart"
urlpatterns = [
    path('cart', cart, name="cart"),
    path('addCart/<int:product_id>', addCart, name="addCart"),
    path('deleteCart/<int:cart_id>', deleteCart, name="deleteCart"),
    path('updateCart/<int:cart_id>', updateCart, name="updateCart"),
    path('purchase/', purchase, name="purchase"),
    path('purchasePage/', purchasePage, name="purchasePage"),
]