from django.shortcuts import render

# 3주차
# REST framework
from .serializers import ProductSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import responses

from contents.models import Product, Category, Brand


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


# 삼품 목록에서 브랜드 별 상품출력
class BrandView(ProductViewSet):
    def get_queryset(self):
        brand = Brand.objects.get(id=self.kwargs['pk'])
        return Product.objects.filter(brand_id=brand)
