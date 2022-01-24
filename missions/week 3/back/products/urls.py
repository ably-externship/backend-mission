from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:object_id>/question/', include('questions.urls'))
]
