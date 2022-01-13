from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.check),

    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),

    # 카카오톡

    path('kakaoLoginLogic/', views.kakaoLoginLogic, name="kakaoLoginLogic"),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name="kakaoLoginLogicRedirect"),
    path('kakaoLogout/', views.kakaoLogout, name="kakaoLogout"),


    # 아이디 찾기
    path('forgot_id/',views.ForgotIDView, name="forgot_id"),

    # 비밀번호 초기화
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
