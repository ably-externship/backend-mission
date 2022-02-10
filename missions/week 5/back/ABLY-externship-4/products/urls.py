from django.urls import include, path
from .customer_views import MerchandiseDetail
from .seller_views import (
    SellerBaseMerchandiseListView,
    SellerMerchandiseCreateView,
    SellerOptionMerchandiseCreateView,
    SellerBaseMerchandiseUpdateDeleteView,
    SellerOptionMerchandiseUpdateDeleteView,
    SuperuserMerchandiseListView,
    SuperuserMerchandiseCreateView,
    SuperuserOptionMerchandiseCreateView,
    SuperuserBaseMerchandiseUpdateDeleteView,
    SuperuserOptionMerchandiseUpdateDeleteView
)


app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>', MerchandiseDetail.as_view(), name='product_detail'),
    path('seller/merchandises', SellerBaseMerchandiseListView.as_view(), name='seller_products'),
    path('seller/merchandises/new', SellerMerchandiseCreateView.as_view(), name='seller_new_products'),
    path('seller/merchandises/option/new', SellerOptionMerchandiseCreateView.as_view(), name='seller_add_option_product'),
    path('seller/merchandises/<str:code>', SellerBaseMerchandiseUpdateDeleteView.as_view(), name='seller_update_or_delete_product'),
    path('seller/merchandises/option/<str:code>', SellerOptionMerchandiseUpdateDeleteView.as_view(), name='seller_update_or_delete_option_product'),
    path('superuser/merchandises', SuperuserMerchandiseListView.as_view(), name='all_products'),
    path('superuser/merchandises/new', SuperuserMerchandiseCreateView.as_view(), name='superuser_new_products'),
    path('superuser/merchandises/option/new', SuperuserOptionMerchandiseCreateView.as_view(), name='superuser_add_option_product'),
    path('superuser/merchandises/<int:pk>', SuperuserBaseMerchandiseUpdateDeleteView.as_view(), name='superuser_update_or_delete_product'),
    path('superuser/merchandises/option/<int:pk>', SuperuserOptionMerchandiseUpdateDeleteView.as_view(), name='superuser_update_or_delete_option_product'),
]