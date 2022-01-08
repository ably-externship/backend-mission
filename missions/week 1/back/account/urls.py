from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from account.views import (
    AccountDetailView,
    AccountUpdateView,
    AccountCreateView,
    AccountDeleteView,
    UserPasswordResetView,
    UserPasswordResetDoneView, find_username_view,
)


app_name = "account"

urlpatterns = [
    path('signup/', AccountCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('find_username', find_username_view, name='find_username'),
]
