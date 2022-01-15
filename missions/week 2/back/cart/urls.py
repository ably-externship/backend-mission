from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/<int:product_id>/', views.add, name='product_add'),
    path('remove/<product_id>/', views.remove, name='product_remove'),
]