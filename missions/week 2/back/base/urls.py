from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base, name='home_page'),
    path('m', views.main, name='main_page'),
    path('shop/<int:id>', views.shop, name="shop_page"),
    path('shop/<int:id>/item/<int:num>', views.item, name="item_page"),
    path('search/', views.search, name="search_page"),
]