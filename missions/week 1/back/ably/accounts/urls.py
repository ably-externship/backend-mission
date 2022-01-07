from django.urls import path

from accounts.signup_views import SignUpView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
]