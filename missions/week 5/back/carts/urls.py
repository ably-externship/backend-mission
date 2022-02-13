from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('cart/<product_id>', views.add_cart, name='add_cart'),
    path('cart/plus/<product_id>', views.plus_cart, name='plus_cart'),
    path('cart/minus/<product_id>', views.minus_cart, name='minus_cart'),
    path('cart/delete/<product_id>', views.delete_cart, name='delete_cart'),
]
