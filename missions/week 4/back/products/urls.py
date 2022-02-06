from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:object_id>/question/', include('questions.urls'))
]
