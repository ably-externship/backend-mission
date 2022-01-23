from django.urls import path
from .views import *

app_name = 'manager'

urlpatterns = [
    path('', ProductList.as_view(), name="list"),
    path('<int:pk>', ProductDetail.as_view(), name="detail"),
    path('delete/<int:pk>', DeleteProduct.as_view(), name="delete"),
    path('product-inventory/<int:product_id>', InventoryCreate.as_view(), name="inventory"),
    path('inventory/<int:pk>', ProductInventory.as_view()),
]