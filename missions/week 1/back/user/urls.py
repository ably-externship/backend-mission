from django.urls import path
from django.contrib.auth import views as auth_views
from user import views

app_name = 'user'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('result/', views.result, name='result'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]