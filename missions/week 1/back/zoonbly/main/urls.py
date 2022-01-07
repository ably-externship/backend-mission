from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', home, name="home"),
    path('productNew/', productNew, name="productNew"),
    path('prodectCreate/', productCreate, name="productCreate"),
    path('productDetail/<int:id>', productDetail, name="productDetail"),
    path('productEdit/<int:id>', productEdit, name="productEdit"),
    path('productUpdate/<int:id>', productUpdate, name="productUpdate"),
    path('productDelete/<int:id>', productDelete, name="productDelete"),
]