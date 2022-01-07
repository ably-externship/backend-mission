from django.urls import path
from updatedb.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', updatedb, name='updatedb'),
]