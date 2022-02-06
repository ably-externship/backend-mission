from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.ProductViewSet)

router2 = NestedDefaultRouter(router, r'', lookup='product')
router2.register(r'options', views.ProductOptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
]
