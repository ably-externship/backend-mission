from django.urls import include, path

from api import views

# django rest framework
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)

detail_router = NestedSimpleRouter(router, r'product', lookup='product')
detail_router.register(r'productdetail', views.ProductDetailViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(detail_router.urls)),
]