from django.urls import path,include
from .views import (cart_delete, cart_list,cart_add, cart_update,
                    product_purchase)
"""
ENDPOINT : cart/

"""
app_name = 'cart'
urlpatterns = [
    path('list',cart_list,name='list'),
    path('add',cart_add,name='add'),
    path('update',cart_update,name='update'),
    path('delete',cart_delete,name='delete'),
    
    path('purchase',product_purchase,name = 'purchase')
]