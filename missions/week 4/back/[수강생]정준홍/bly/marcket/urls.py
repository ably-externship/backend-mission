from unicodedata import name
from django.urls import path
from .views import *

app_name = "marcket"
urlpatterns = [
    path('', marcket_create, name='marcket_create'),
    path('<int:marcket_pk>/', marcket_detail_update_delete, name='marcket_deatail_update_delete'),
    path('<int:marcket_pk>/products/',product_create,name='product_create'),
    path('<int:marcket_pk>/products/<int:product_pk>/',product_detail_update_delete,name='product_detail_update_delete'),
    path('<int:marcket_pk>/products/<int:product_pk>/options/',option_create,name='option_create'),
    path('<int:marcket_pk>/products/<int:product_pk>/options/<int:option_pk>', option_detail_update_delete,name='option_detail_update_delete'),
]