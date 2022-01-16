from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/detail/', views.detail, name='detail'),
    path('<int:product_id>/detail/write/', views.write, name='write'),
    path('<int:product_id>/detail/add_cart/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/detail_change/<int:detail_id>/', views.detail_change, name='detail_change'),
    path('cart/item_delete/<int:detail_id>/', views.item_delete, name='item_delete'),
    path('pay/', views.pay, name='pay'),
]
