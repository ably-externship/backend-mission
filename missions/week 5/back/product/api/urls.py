from django.urls import path
from product.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CartItemListAPIView,
    CartItemDetailAPIView,
    OrderItemListAPIView,
    OrderItemDetailAPIView,
    OrderedItemListAPIView,
)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('cartitems/', CartItemListAPIView.as_view()), # 장바구니
    path('cartitems/<int:pk>/', CartItemDetailAPIView.as_view()),
    path('orderitems/', OrderItemListAPIView.as_view()), # 주문
    path('orderitems/<int:pk>/', OrderItemDetailAPIView.as_view()),
    path('ordereditems/', OrderedItemListAPIView.as_view(),)
]

