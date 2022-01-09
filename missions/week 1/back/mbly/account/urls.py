from django.contrib import admin
from django.conf import settings
from django.urls import path
# from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from .views import signup

"""
endpoint : account/
"""

app_name = 'account'

urlpatterns = [
    path('login',auth_views.LoginView.as_view(template_name = 'account/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('signup',signup,name = 'signup'),
]
