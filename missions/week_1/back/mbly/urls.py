from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('api/v1/user/login')),
    path('api/', include('api.urls', 'api')),
    path('admin/', admin.site.urls),
]
