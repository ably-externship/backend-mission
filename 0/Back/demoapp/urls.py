from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoGeneralView.as_view()),
    path('<int:pk>/', views.TodoSepcView.as_view()),
]