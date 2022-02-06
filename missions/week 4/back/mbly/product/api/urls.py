from django.urls import path,include
from .views import ProductList,ProductDetail,ProductMarketList,ProductMarketDetail,RealProductList
"""
ENDPOINT : api/product/

"""
app_name = 'product_api'
urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:pk>',ProductDetail.as_view()),
    path('market',ProductMarketList.as_view()),
    path('market/<int:product_id>',ProductMarketDetail.as_view()),

    path('options',RealProductList.as_view()),
    path('options/<int:option_id>',RealProductList.as_view()),
]