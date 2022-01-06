from django.urls import path, include

urlpatterns = [
    path('v1/user/', include('user.urls')),
    path('v1/product/', include('product.urls')),
]