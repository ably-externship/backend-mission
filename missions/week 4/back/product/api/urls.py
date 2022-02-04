from django.urls import path, include
from product.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    product_create_or_list,
    product_detail,
)


urlpatterns = [
    path('', product_create_or_list),
    path('<int:pk>/', product_detail),

    path('marketowner/', ProductListAPIView.as_view()),
    path('marketowner/<int:pk>/', ProductDetailAPIView.as_view()),


]
