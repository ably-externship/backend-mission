from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/question/", views.question, name="question"),
    path('search/', views.search, name='search'),
]
