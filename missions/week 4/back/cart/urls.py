from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/', add_cart, name='add_cart'),
    path('', cart_list, name = 'list'),
    path('<int:cart_id>', cart_delete, name='cart_delete'),
    path('qty/<int:cart_id>', cart_modify, name='cart_modify'),
]