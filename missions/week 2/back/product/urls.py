from django.urls import path, include
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('search', views.search, name='search'),
    path('create/<int:product_id>', views.create, name='create'),
]
