from django.urls import path

from products.detail_views import ProductDetailView

urlpatterns = [
    path('/detail/<int:product_id>', ProductDetailView.as_view()),
]