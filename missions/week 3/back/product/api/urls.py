from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.api.views import product_create_or_list, product_detail

# from product.api.views import ProductViewSet

# TODO: SimpleRouter vs DefaultRouter 차이점
# router = SimpleRouter()
# router.register('', ProductViewSet)


urlpatterns = [
    # POST /api/products/cart/change_quantity/
    # path('cart/change_quantity/', change_quantity_api_view),

    # DELETE /api/products/cart/:cart_item_id/
    # path('cart/:cart_item_id/', cart_delete_view, name='cart_delete'),

    # path('', include(router.urls)),

    # REST 개념

    # Rest 에서는 리소스 정의,
    # 생성 POST /{리소스}
    #

    # 상품 추가 : POST /api/products/
    # 상품 목록 조회 : GET /api/products/
    path('', product_create_or_list),

    # 상품 상세 조회 : GET /api/products/<int:pk>/
    # 상품 수정 : PUT /api/products/products/<int:pk>/
    # 상품 삭제 : DELETE /api/products/products/<int:pk>/
    path('<int:pk>/', product_detail),


]
