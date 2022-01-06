from django.urls import path
from .views import allItem, itemSearch, itemIndex
urlpatterns = [
    path('items', itemIndex, name="item_index"),
    path('items/all', allItem, name="all_item_list"),
    path('items/search', itemSearch, name="item_search"),
]