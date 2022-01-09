
from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views

# app_name= 'accounts'

# urlpatterns = [
#   # path('signup/', views.signup, name='signup'),
#   path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
# ]
