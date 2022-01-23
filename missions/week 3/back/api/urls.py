from django.urls import include, path
from api import views

# django rest framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('productdetail', views.ProductDetailViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]