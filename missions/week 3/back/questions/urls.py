from django.urls import path

from . import views

urlpatterns = [
    path('', views.question, name='question'),
    path('submit/', views.question_submit, name='question_submit')
]
