from django.urls import path
from product.views import (
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    product_list_view, add_cart_view, cart_items_view,
)

app_name = 'product'

urlpatterns = [
    path('list/', product_list_view, name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('add_cart/', add_cart_view, name='add_cart'),
    path('cart_items/', cart_items_view, name='cart_items')
]
