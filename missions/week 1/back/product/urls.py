from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/detail/', views.detail, name='detail'),
    path('<int:product_id>/detail/write/', views.write, name='write')
]