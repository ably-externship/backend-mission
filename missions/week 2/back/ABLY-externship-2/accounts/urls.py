from django.urls import include, path
from .views import UserLogin, UserLogout, UserSignup, SocialLogin


app_name = 'accounts'

urlpatterns = [
    path('signup', UserSignup.as_view(), name='signup'),
    path('login', UserLogin.as_view(), name='login'),
    path('login/social/kakao', SocialLogin.as_view(), name='kakao_login'),
    path('logout', UserLogout.as_view(), name='logout'),
]