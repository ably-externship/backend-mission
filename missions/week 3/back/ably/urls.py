from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts', include('accounts.urls')),
    path('products', include('products.urls')),
    path('qnas', include('qnas.urls')),
]