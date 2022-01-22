
from rest_framework import routers
from restapi.views import *
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', helloAPI),
    path('mallslist/', mallsList, name='mallslist'),
    path('mallsitems/<str:pk>/', mallsItems, name='mallsitems'),
    path('mall-create/', mallsCreate, name='mall-create'),
    path('mall-update/<str:pk>/', mallsUpdate, name='mall-update'),
    path('mall-delete/<str:pk>/', mallsDelete, name='mall-delete'),
    path('itemlist/', itemList, name='itemlist-all'),
    path('item-create/<str:pk>/', itemCreate, name='item-create'),
    path('item-update/<str:pk>/<str:num>/', itemUpdate, name='item-update'),
    path('item-delete/<str:pk>/<str:num>/', itemDelete, name='item-delete'),
    
    # generics 뷰
    path('mall-view/', mallView.as_view() , name='mall-view'),
    path('mall-list/', mallListView.as_view() , name='mall-view'),
]