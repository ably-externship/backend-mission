"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mall.urls')),
    #path('mall/', include('mall.urls')),
    path('product/', include('product.urls')),
    path('user/', include('lionuser.urls')),
    path('board/', include('board.urls')),

    path('api/token/', obtain_jwt_token),
    # re_path(r'^rest-auth/', include('rest_auth.urls')),
    # re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # path('api/token/verify/', verify_jwt_token),
    # path('api/token/refresh/', refresh_jwt_token),

]
