from django.urls import path
from . import views

urlpatterns = [
    path('my_cart', views.my_cart, name='cart_page'),
    path('add/<int:id>/<int:num>', views.add_cart, name='add_cart'),
    path('delete/<int:id>/<int:num>', views.delete_cart, name='delete_cart'),
    path('edit/<int:id>/<int:num>', views.edit_cart, name='edit_cart'),
]