from django import views
from django.urls import path
from .views import *

app_name = "cart"
urlpatterns = [
    # 사용자별 장바구니 페이지
    path('cart', cart, name="cart"),

    # 사용자별 장바구니 추가 수정 삭제
    path('addCart/<int:product_id>', addCart, name="addCart"),
    path('deleteCart/<int:cart_id>', deleteCart, name="deleteCart"),
    path('updateCart/<int:cart_id>', updateCart, name="updateCart"),

    # 사용자 별 상품 구매
    path('purchase/<int:categoNum>', purchase, name="purchase"),
    path('purchasePage/', purchasePage, name="purchasePage"),
]