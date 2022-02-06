from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('profile', user_profile, name='user_profile'),
    path('update-page', profile_update_page, name='update_page'),
    path('update', profile_update, name='update'),
]
