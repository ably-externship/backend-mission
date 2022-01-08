from django.urls import path

from products.detail_views import ProductDetailView
from products.list_views import ProductListView

urlpatterns = [
    path('/detail/<int:product_id>', ProductDetailView.as_view()),
    path('/list', ProductListView.as_view()),
]