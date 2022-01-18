from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/', views.add, name='cart_add'),
    path('remove/<cart_id>/', views.remove, name='product_remove'),
]