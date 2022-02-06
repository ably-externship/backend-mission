from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "user"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('users/login/kakao', views.KakaoSignInView.as_view(), name='login_kakao'),
    path('users/login/kakao/callback',
         views.KakaoSignInCallBackView.as_view(), name='login_kakao_callback'),
]


# urlconf: mapping path and function(view)
