from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("logout/", views.logout_view, name="logout"),
]
