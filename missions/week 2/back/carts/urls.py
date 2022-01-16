from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('<int:cart_id>/edit/', views.edit_cart, name='edit_cart'),
    path('<int:cart_id>/remove/', views.remove_from_cart, name='remove_from_cart'),
]
