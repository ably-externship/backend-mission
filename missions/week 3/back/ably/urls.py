from django.urls import path, include

from products.master_views import ProductView

urlpatterns = [
    path('accounts', include('accounts.urls')),
    path('products', include('products.urls')),
    path('qnas', include('qnas.urls')), 
    path('admin/products', ProductView.as_view()),
    path('admin/products/<int:product_id>', ProductView.as_view()),
]