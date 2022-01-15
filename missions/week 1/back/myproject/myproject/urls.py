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

import product.views
import account.views
import board.views

app_name = "account"
urlpatterns = [
    path("admin/", admin.site.urls),
    # 상품들 나열된 페이지
    # path("/", product.views.bottom_view, name="test"),
    path("main/", product.views.bottom_view, name="product"),
    # 상품 디테일 페이지
    path("detail/", product.views.detail_view, name="detail"),
    # 회원가입
    path("signup/", account.views.signup, name="signup"),
    # 로그인
    path("login/", account.views.login, name="login"),
    path("login/", account.views.logout, name="logout"),
    #
    path("board/", board.views.board, name="board"),
    path("search/", product.views.searchItem, name="search"),
]
