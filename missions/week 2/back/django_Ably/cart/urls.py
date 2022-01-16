from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    # path('add/<int:item_id>/',views.add_cart, name='add_cart'),
    # path('',views.cart_detail, name='cart_detail'),
    path('',views.view_cart, name='view_cart'),
    path('add',views.add_cart, name='add_cart'),
    path('update/<int:pk>/',views.update, name='update'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]
