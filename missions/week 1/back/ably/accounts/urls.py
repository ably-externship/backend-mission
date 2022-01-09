from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # 회원가입
    path('sign-up/', views.sign_up, name='sign_up'),
    # 로그인
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]