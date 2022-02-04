from django.urls import path
from .views import allItem, itemSearch, itemIndex, ProductViewSet, ProductImgViewSet, BillingRecordsView, \
    search_by_elastic, MarketAdminProductListCreateView, MarketAdminProductRetrieveUpdateDestroyView, \
    MarketAdminApiProductRealListCreateView

urlpatterns = [ #
    path('items', itemIndex, name ="item_index"),
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
    path('search_by_elastic/', search_by_elastic, name='search_by_elastic'),

    path('market_admin_api/', MarketAdminProductListCreateView.as_view(), name='market_admin_api'),
    path('market_admin_api/<int:pk>/', MarketAdminProductRetrieveUpdateDestroyView.as_view(), name='market_admin_api_item'),
    path('market_admin_api/<int:product_id>/reals/', MarketAdminApiProductRealListCreateView.as_view(), name='market_admin_api_reals'),
]


