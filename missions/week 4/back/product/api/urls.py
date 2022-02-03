from django.urls import path, include
from product.api.views import ProductListAPIView, ProductDetailAPIView, PostViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('product', PostViewSet)


urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),

    path('test/', include(router.urls))
]
