from django.urls import path
from product.api.views import (
    ProductListView,
    ProductDetailView,
    CartItemListView,
    CartItemDetailView,
    CartItemOrderView,
    OrderItemListView,
    OrderItemDetailView,
    OrderedItemListView,
    OrderedItemDetailView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('cart/items/', CartItemListView.as_view()), # 장바구니
    path('cart/items/<int:pk>/', CartItemDetailView.as_view()),
    path('cart/item/orders/', CartItemOrderView.as_view()),
    path('order/items/', OrderItemListView.as_view()), # 주문
    path('order/items/<int:pk>/', OrderItemDetailView.as_view()),
    path('ordered/items/', OrderedItemListView.as_view()),
    path('ordered/items/<int:pk>/', OrderedItemDetailView.as_view()),


]


