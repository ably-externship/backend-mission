from django.urls import path,include
from .views import MarketList,MarketDetail
"""
ENDPOINT : api/market/

"""
app_name = 'market_api'
urlpatterns = [
    path('',MarketList.as_view()),
    path('<int:product_id>',MarketDetail.as_view())
]