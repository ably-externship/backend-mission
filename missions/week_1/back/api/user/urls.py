from django.urls import path
from ..user import views

app_name = 'user'

urlpatterns = [
    path('login', views.login_view),
    path('logout', views.LogoutView.as_view()),
    path('register', views.register_view),
]