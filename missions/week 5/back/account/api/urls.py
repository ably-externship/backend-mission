from django.urls import path

from account.api.views import SignupUserView, LoginView, LogoutView, ChangePasswordView

urlpatterns = [
    path('signup/', SignupUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
]

