from django.urls import path

from accounts.signup_views import SignUpView
from accounts.login_views import LogInView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LogInView.as_view()),
]