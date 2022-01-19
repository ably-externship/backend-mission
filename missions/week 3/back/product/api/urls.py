from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.api.views import ProductViewSet

# TODO: SimpleRouter vs DefaultRouter 차이점
router = SimpleRouter()
router.register('', ProductViewSet)


urlpatterns = [
    # POST /api/products/cart/change_quantity/
    # path('cart/change_quantity/', change_quantity_api_view),

    # DELETE /api/products/cart/:cart_item_id/
    # path('cart/:cart_item_id/', cart_delete_view, name='cart_delete'),

    path('', include(router.urls)),
]
