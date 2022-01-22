
from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views


app_name= 'accounts'

urlpatterns = [
  path('', include('django.contrib.auth.urls')),
  path('signup/', views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('forgot_id/', views.forgot_id, name='find_id'),
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  # path('social_accounts/', include('allauth.urls')),
]
