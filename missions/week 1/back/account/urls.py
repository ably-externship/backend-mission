from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from account.views import (
    AccountCreateView,
    find_username_view,
    reset_password_view,
    change_password_view,
)

app_name = "account"

urlpatterns = [
    path('signup/', AccountCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('find_username/', find_username_view, name='find_username'),
    path('reset_password/', reset_password_view, name='reset_password'),
    path('change_password/', change_password_view, name='change_password'),

]
