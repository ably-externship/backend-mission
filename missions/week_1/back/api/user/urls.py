from django.urls import path
from ..user import views

app_name = 'user'

urlpatterns = [
    path(r'login', views.LoginView.as_view()),
    path(r'registration', views.RegisterView.as_view()),
    path(r'logout', views.logout),
]