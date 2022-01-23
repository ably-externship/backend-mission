"""base URL Configuration
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as UserViews
from django.contrib.auth import views as auth_views

from manager.views import BlacklistTokenUpdateView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # my_app
    path('', include('shop.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('seller/', include('seller.urls')),

    # drf
    path('manager/', include('manager.urls')),
    path('manager-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('manager/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('manager/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('manager/logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),

    # 소셜로그인
    path('accounts/', include('allauth.urls')),

    # 로그인
    path('login/', UserViews.login_form, name='login'),
    path('join/', UserViews.signup_form, name='join'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)