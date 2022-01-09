from django.urls import path,include
from .views import ProductDetail, ProductList

"""
ENDPOINT : product/

"""
app_name = 'product'
urlpatterns = [
    path('list',ProductList.as_view(),name='list'),
    path('detail/<int:pk>',ProductDetail.as_view(),name='detail'),
    
]