from django.urls import path
from product.api.views import product_create_or_list, product_detail

urlpatterns = [
    path('', product_create_or_list),
    path('<int:pk>/', product_detail),
]
