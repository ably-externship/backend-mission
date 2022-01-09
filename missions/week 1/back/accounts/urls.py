from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('register_succeeded/', views.register_succeeded, name='register_succeeded'),
    path('recovery/', views.recovery, name='recovery'),
    path('recovery_done/', views.recovery_done, name='recovery_done'),
]
