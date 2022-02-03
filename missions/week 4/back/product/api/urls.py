from django.urls import path
from product.api.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
]
