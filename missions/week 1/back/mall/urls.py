from django.urls import path
from .views import index, shop_item, shop_item_detail, ShopViewSet, shop_qna_create, qna_list

urlpatterns = [
    path('shop', ShopViewSet.as_view({
        'post':'create'
    })),
    path('', index, name="shop"),
    path('shop/<int:shop>/items', shop_item, name="item_list"),
    path('shop/<int:shop>/items/<int:item>',shop_item_detail, name="item"),
    path('shop/<int:shop>/qna', shop_qna_create, name="qna"),
    path('shop/<str:pk>/qna-list', qna_list, name="qna_list"),

]

