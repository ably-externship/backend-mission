from django.urls import path,include
from .views import ProductList,ProductDetail
"""
ENDPOINT : api/product/

"""
app_name = 'product'
urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:product_id>',ProductDetail.as_view())
]