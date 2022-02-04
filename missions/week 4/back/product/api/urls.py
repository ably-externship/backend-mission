from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    product_create_or_list,
    product_detail, PostViewSet,
)

router = DefaultRouter()
router.register("posts", PostViewSet)


urlpatterns = [
    path('', product_create_or_list),
    path('<int:pk>/', product_detail),

    path('marketowner/', ProductListAPIView.as_view()),
    path('marketowner/<int:pk>/', ProductDetailAPIView.as_view()),

    path('test/', include(router.urls)),


]
