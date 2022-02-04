from django.urls import path
from .views import allItem, itemSearch, itemIndex, ProductViewSet, ProductImgViewSet, BillingRecordsView

urlpatterns = [
    path('items', itemIndex, name="item_index"),
    path('items/all', allItem, name="all_item_list"),
    path('items/search', itemSearch, name="item_search"),
    path('asdf/', BillingRecordsView.as_view(), name="itearch"),

    path('admin', ProductViewSet.as_view({

# 'get':'get_queryset',
         'get': 'list',
        'post': 'create'
    })),
    path('admin/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    #url 에 admin 붙여도 되는지

    path('img', ProductImgViewSet.as_view({

        'get': 'list',
        'post': 'create'
    })),
    path('img/<str:pk>', ProductImgViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]