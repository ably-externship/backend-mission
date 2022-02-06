from django.contrib import admin
from django.conf import settings
from django.urls import path
# from django.contrib.auth.views import LoginView,LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserInfoView
"""
endpoint : api/account/
"""

urlpatterns = [
    path('token',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('token/verify',TokenVerifyView.as_view()),
    path('token/info/',UserInfoView.as_view())
]
