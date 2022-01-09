from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/question', views.question, name='question'),
    path('<int:product_id>/question_submit', views.question_submit, name='question_submit')
]
