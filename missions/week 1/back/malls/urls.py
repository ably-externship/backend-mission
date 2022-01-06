from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main/', views.main, name='main_page'),
    path('login/', views.login, name='login_page'),
]