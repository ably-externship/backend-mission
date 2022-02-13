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

from manager.views import BlacklistTokenUpdateView, ManagerTokenObtainPairView
from seller.views import SellerTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # my_app
    path('', include('shop.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('review/', include('review.urls')),

    # drf app
    path('api/manager/', include('manager.urls')),
    path('api/seller/', include('seller.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf jwt
    path('api/token-manager/', ManagerTokenObtainPairView.as_view(), name='token_obtain_pair_manager'),
    path('api/token-seller/', SellerTokenObtainPairView.as_view(), name='token_obtain_pair_seller'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),

    # 소셜로그인
    path('accounts/', include('allauth.urls')),

    # 로그인
    path('login/', UserViews.login_form, name='login'),
    path('join/', UserViews.signup_form, name='join'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)