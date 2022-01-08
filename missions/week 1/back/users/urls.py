from django.urls import path
from . import views
from .views import email_duplicate_check

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_call),
    path('sign-up/', views.sign_up),
    path('dup-check/', email_duplicate_check)
]