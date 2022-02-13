from django import views
from django.urls import path
from .views import *

app_name="manager"
urlpatterns = [
    path('', product_list_create),
    path('<int:product_pk>/', product_detail_update_delete),
]