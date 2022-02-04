from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.api.permission import IsOwner
from product.api.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from product.models import Product


class PageNumberPagination(PageNumberPagination):
    page_size = 10


class ProductListAPIView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):

        # staff
        if request.user.is_staff:
            qs = Product.objects.filter(author=request.user)
            serializer = ProductSerializer(qs, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            qs = Product.objects.all()
            serializer = ProductSerializer(qs, many=True, context={'request': request})
            return Response(serializer.data)

    def post(self, request):
        # 관리자 or staff
        if request.user.is_superuser or request.user.is_staff:
            author = self.request.user
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=author)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    pagination_class = PageNumberPagination
    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            qs = Product.objects.get(pk=pk)
            self.check_object_permissions(self.request, qs)
            return qs
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product, context={'request': request})
        return Response(serializer.data)

    def patch(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
