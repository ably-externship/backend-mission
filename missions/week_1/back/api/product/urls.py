from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.ProductListView.as_view()),
    path('search/', views.ProductSearchView.as_view()),
    path('detail/', include('api.products.detail.urls', 'detail'))
]