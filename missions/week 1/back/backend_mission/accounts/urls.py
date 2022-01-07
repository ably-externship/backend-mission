from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import AccountDetailView, AccountUpdateView, AccountCreateView, AccountDeleteView


app_name = "accounts"

urlpatterns = [

    path('signup/', AccountCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),



]
