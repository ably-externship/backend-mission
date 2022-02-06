from django.urls import path
from .views import *

app_name = 'seller'

urlpatterns = [
    path('register', register, name='register'),

    path('', SellerProduct.as_view(), name='seller_product'),
    path('account', SellerAccount.as_view(), name='seller_reg'),
    path('<int:product_id>', SellerProductEdit.as_view(),name='seller_prod_edit'),
    path('option/<int:product_id>', SellerProductOption.as_view(), name='seller_prod_opt'),
    path('option/<int:product_id>/<int:inventory_id>', SellerProductOptionEdit.as_view(), name='seller_prod_opt_edit'),
]
