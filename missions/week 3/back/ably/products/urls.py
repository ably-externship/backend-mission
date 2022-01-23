from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'products'
urlpatterns = [
    # 쇼핑몰 상품 리스트
    path('', views.index, name='index'),
    # 쇼핑몰 상품 상세페이지
    path('<int:product_id>/', views.detail, name='detail'),
    # 상품질문기능
    path('<int:product_id>/question/', views.question, name='question'),
    # 장바구니 품목 추가
    path('<int:product_id>/add/', views.add, name='add'),
    # 장바구니 보기
    path('basket/', views.basket, name='basket'),
    # 장바구니 품목 수정: 수량
    path('basket/<int:id>/update/', views.basket_update, name='basket_update'),
    # 장바구니 품목 삭제
    path('basket/<int:id>/delete/', views.basket_delete, name='basket_delete'),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
