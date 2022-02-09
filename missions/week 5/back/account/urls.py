from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from account.views import (
    AccountCreateView,
    find_username_view,
    reset_password_view,
    change_password_view, oauth, kakao_login_view,
)
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

app_name = "account"

urlpatterns = [
    path('signup/', AccountCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('kakao_login/', kakao_login_view, name='kakao_login'),
    path('oauth/', oauth, name='oauth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('find_username/', find_username_view, name='find_username'),
    path('reset_password/', reset_password_view, name='reset_password'),
    path('change_password/', change_password_view, name='change_password'),

    path('token/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token), # 검증

]
