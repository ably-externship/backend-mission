from django.urls import path

from accounts.signup_views import SignUpView
from accounts.login_views import LogInView
from accounts.kakao_login_views import KakaoLoginView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LogInView.as_view()),
    path('/login/kakao', KakaoLoginView.as_view()),
]