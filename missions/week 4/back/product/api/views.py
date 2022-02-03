from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from product.api.permission import IsOwner
from product.api.serializers import ProductSerializer
from product.models import Product


# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
#
#
# def list_product():
#     serializer = ProductSerializer(Product.objects.all(), many=True)
#     return Response(serializer.data)
#
#
# def retrieve_product(product):
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
#
#
# def update_product(product, request):
#     serializer = ProductSerializer(product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# def delete_product(product):
#     product.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def product_create_or_list(request):
#     if request.method == 'GET':
#         return list_product()
#     else:
#         return create_product(request)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return retrieve_product(product)
#     elif request.method == 'PUT':
#         return update_product(product, request)
#     else:
#         return delete_product(product)
#


class ProductListAPIView(APIView):

    permission_classes = [IsOwner]

    def get(self, request):
        qs = Product.objects.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    def put(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



