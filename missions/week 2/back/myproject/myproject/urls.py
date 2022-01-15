"""myproject URL Configuration

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
from django.urls import path
from django.conf.urls import include
from django.urls import re_path

import products.views
import accounts.views
import boards.views


urlpatterns = [
    path("admin/", admin.site.urls),
    #
    path("main/", products.views.main, name="product"),
    path("detail/", products.views.detail_view, name="detail"),
    path("search/", products.views.searchItem, name="search"),
    #
    path("login/", accounts.views.login, name="login"),
    path("logout/", accounts.views.logout, name="logout"),
    path("signup/", accounts.views.signup, name="signup"),
    #
    path("board/", boards.views.board, name="board"),
    #
    path("accounts/", include("allauth.urls")),
    path("kakao/", accounts.views.kakao, name="kakao"),
]
