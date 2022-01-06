from django.urls import path, include
from ..product import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListView.as_view()),
    path('search/', views.ProductSearchView.as_view()),
    path('detail/', include('api.product.detail.urls', 'detail'))
]