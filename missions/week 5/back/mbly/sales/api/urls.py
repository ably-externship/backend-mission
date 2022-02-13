from django.urls import path,include
from .views import ProductDailyDetail,ProductDailyList,MarketDailyList,MarketDailyDetail

"""
ENDPOINT : api/sales/

"""
urlpatterns = [
    path('',ProductDailyList.as_view()),
    path('<int:product_id>',ProductDailyDetail.as_view()),

    path('market',MarketDailyList.as_view()),
    path('mymarket',MarketDailyDetail.as_view()),
]