from django.urls import path
from ..user import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('register', views.RegisterView.as_view()),
]