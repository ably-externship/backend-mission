from django.shortcuts import render

# 3주차
# REST framework
from .serializers import ProductSerializer, BrandSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import responses

from contents.models import Product, Category, Brand

# 4주차
from rest_framework import permissions
from .permission import MasterSerializer, IsOwnerOrReadOnly



# 3주차
# 상품 목록 및 상세 화면 API
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer


# 상품 목록에서 카테고리 별 상품출력
class CategoryView(ProductViewSet):
     def get_queryset(self):
         category = Category.objects.get(id=self.kwargs['pk'])
         return Product.objects.filter(category_id=category)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('pk')
    serializer_class = BrandSerializer


brands_list = BrandViewSet.as_view(
    {'get': 'list',
     'post': 'create',
     })

brands_detail = BrandViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# # 삼품 목록에서 브랜드 별 상품출력
# class BrandView(viewsets.ModelViewSet):
#     queryset = Brand.objects.all().order_by('pk')
#     serializer_class = BrandSerializer


# 삼품 목록에서 브랜드 별 상품출력
class BrandView(ProductViewSet):
    def get_queryset(self):
        brand = Brand.objects.get(id=self.kwargs['pk'])
        return Product.objects.filter(brand_id=brand)


# 4주차
class BrandMasterView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, MasterSerializer]

    def get_queryset(self):
        return Product.objects.filter(brand=self.request.user.brand)

    def perform_create(self, serializer):
        brand = self.request.user.brand
        serializer.save(brand=brand)






