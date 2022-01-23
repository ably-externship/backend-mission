from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'product'

urlpatterns = format_suffix_patterns([
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('search', views.search, name='search'),
    path('comment/<int:product_id>', views.create_comment, name='create_comment'),

    path('admin/products/', views.ProductList.as_view()),
    path('admin/products/<int:pk>/', views.ProductDetail.as_view()),
    
    path('admin/vendors/', views.VendorList.as_view()),
    path('admin/vendors/<int:pk>/', views.VendorDetail.as_view()),

])