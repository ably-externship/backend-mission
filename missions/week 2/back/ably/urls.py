"""ably URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from contents.views import HomeView, ProductListView, ProductDetailView, SearchView, CategoryView, BrandView, CartView


# NonUserTemplateView 를 사용하는 이유는 로그인과 회원가입 페이지에서 사용자의 접근을 막기위함
class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('/')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # apis app urls.py connect
    path('apis/', include('apis.urls')),

    # product
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/category/<str:slug>/', CategoryView.as_view(), name='category_product_list'),
    path('product/brand/<str:slug>/', BrandView.as_view(), name='brand_product_list'),

    # cart
    path('cart/', CartView.as_view(), name='cart'),

    # search
    path('product/search/<str:q>/', SearchView.as_view(), name="search"),

    # user
    path('login/', NonUserTemplateView.as_view(template_name='user/login.html'), name='login'),
    path('register/', NonUserTemplateView.as_view(template_name='user/register.html'), name='register'),
]
