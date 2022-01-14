from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('cart/',views.cart,name="cart"),
    # path('cart_detail/',views.cart_detail,name="cart_detail"),

]
