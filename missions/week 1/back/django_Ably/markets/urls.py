from django.urls import path
from . import views

urlpatterns = [
    path('markets/', views.page, name='page'),
]