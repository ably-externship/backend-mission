from django.urls import path
import apis.views
from rest_framework import routers
from django.conf.urls import include 
from .views import ItemViewSet



router = routers.DefaultRouter()

#apis for items CRUD
router.register('items', ItemViewSet)


app_name = 'apis'

urlpatterns = [
    path('',include(router.urls)), 
]

