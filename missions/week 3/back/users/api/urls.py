from django.urls import path

from .views import get_token, refresh_token

urlpatterns = [
    path('token', get_token),
    path('refresh', refresh_token)
]
