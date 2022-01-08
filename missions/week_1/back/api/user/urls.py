from django.urls import path
from ..user import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt

app_name = 'user'

urlpatterns = [
    path(r'login', views.login_view),
    path(r'logout', LogoutView.as_view()),
    path(r'register', csrf_exempt(views.register_view)),
]