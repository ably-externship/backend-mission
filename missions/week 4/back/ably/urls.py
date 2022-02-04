from django.urls import path, include

from products.admin_views import ProductView
from core.views import CategoryView, ColorView, SizeView

urlpatterns = [
    path('accounts', include('accounts.urls')),
    path('products', include('products.urls')),
    path('qnas', include('qnas.urls')), 
    path('admin/products', ProductView.as_view()),
    path('admin/products/<int:product_id>', ProductView.as_view()),
    path('categories', CategoryView.as_view()),
    path('colors', ColorView.as_view()),
    path('sizes', SizeView.as_view()),
]