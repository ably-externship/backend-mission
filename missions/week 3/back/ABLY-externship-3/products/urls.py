from django.urls import include, path
from .customer_views import MerchandiseDetail
from .seller_views import (
    SellerBaseMerchandiseListView,
    SuperuserMerchandiseListView,
    SuperuserMerchandiseCreateView,
    SuperuserOptionMerchandiseCreateView,
    SuperuserBaseMerchandiseUpdateDeleteView,
    SuperuserOptionMerchandiseUpdateDeleteView
)


app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>', MerchandiseDetail.as_view(), name='product_detail'),
    path('sellers/merchandises', SellerBaseMerchandiseListView.as_view(), name='seller_products'),
    path('superuser/merchandises', SuperuserMerchandiseListView.as_view(), name='all_products'),
    path('superuser/merchandises/new', SuperuserMerchandiseCreateView.as_view(), name='new_products'),
    path('superuser/merchandises/option/new', SuperuserOptionMerchandiseCreateView.as_view(), name='add_option_product'),
    path('superuser/merchandises/<int:pk>', SuperuserBaseMerchandiseUpdateDeleteView.as_view(), name='update_or_delete_product'),
    path('superuser/merchandises/option/<int:pk>', SuperuserOptionMerchandiseUpdateDeleteView.as_view(), name='update_or_delete_option_product'),
]