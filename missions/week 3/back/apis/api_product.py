from django.shortcuts import render

from .serializers import ProductSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import responses

from contents.models import Product, Comment, Category, Brand


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer


post_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class CategoryView(ProductViewSet):
     def get_queryset(self):
         category = Category.objects.get(id=self.kwargs['pk'])
         return Product.objects.filter(category_id=category)


class BrandView(ProductViewSet):
    def get_queryset(self):
        brand = Brand.objects.get(id=self.kwargs['pk'])
        return Product.objects.filter(brand_id=brand)
