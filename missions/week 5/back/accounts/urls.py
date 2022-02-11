from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.register, name='register'),
    path('register_succeeded/', views.register_succeeded, name='register_succeeded'),
    path('recovery/', views.recovery, name='recovery'),
    path('recovery_done/', views.recovery_done, name='recovery_done'),
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/callback/', views.kakao_login_callback, name='kakao_login_callback'),
]
