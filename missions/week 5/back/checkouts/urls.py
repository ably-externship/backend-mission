from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('submit/', views.submit, name='submit'),
    path('verify/', views.verify, name='verify'),
    path('succeeded/', views.succeeded, name='succeeded'),
    path('list/', views.TransactionListView.as_view(), name='list'),
]
