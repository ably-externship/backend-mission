from django.urls import path,include
from .views import ProductList,ProductDetail
"""
ENDPOINT : api/product/

"""
app_name = 'product_api'
urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:pk>',ProductDetail.as_view())
]