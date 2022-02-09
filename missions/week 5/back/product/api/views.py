from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.api.permission import IsOwner
from product.api.serializers import ProductSerializer, CartItemSerializer, OrderItemSerializer, ProductOptionSerializer
from rest_framework.pagination import PageNumberPagination
from product.models import Product, CartItem, OrderItem, ProductOption


class PageNumberPagination(PageNumberPagination):
    page_size = 10


class ProductListAPIView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        # superuser
        if request.user.is_superuser:
            qs = Product.objects.all()
            serializer = ProductSerializer(qs, many=True, context={'request': request})
            return Response(serializer.data)
        # staff
        elif request.user.is_staff:
            qs = Product.objects.filter(author=request.user)
            serializer = ProductSerializer(qs, many=True, context={'request': request})
            return Response(serializer.data)
        # all
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
        else:
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
        try:
            qs = Product.objects.get(pk=pk)
            serializer = ProductSerializer(qs, context={'request': request})
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

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


# 장바구니
class CartItemListAPIView(APIView):
    def get(self, request):
        qs = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = self.request.user.id
        product_id = request.data['product_id']
        productoption_id = request.data['productoption_id']
        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=user_id, product_id=product_id, productoption_id=productoption_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CartItemDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(CartItem, pk=pk)

    def get(self, request, pk):
        CartItem = self.get_object(pk)
        serializer = CartItemSerializer(CartItem)
        return Response(serializer.data)

    def patch(self, reqeust, pk):
        CartItem = self.get_object(pk)
        serializer = CartItemSerializer(CartItem, data=reqeust.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        CartItem = self.get_object(pk)
        CartItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 주문하기
class OrderItemListAPIView(APIView):
    def get(self, request):
        qs = OrderItem.objects.filter(user=request.user)
        serializer = OrderItemSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        productoption_id = request.data['productoption_id']
        serializer = OrderItemSerializer(data=request.data)

        productoption = ProductOption.objects.get(id=productoption_id)
        stockcount = productoption.stock_count
        stockcount -= 1
        ProductOption.objects.filter(id=productoption_id).update(stock_count=stockcount)

        if serializer.is_valid():
            serializer.save(user_id=user_id, product_id=product_id, productoption_id=productoption_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderItemDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(OrderItem, pk=pk)

    def get(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = OrderItemSerializer(OrderItem)
        return Response(serializer.data)

    def patch(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = OrderItemSerializer(OrderItem, data=request.data, partial=True)
        quantity = request.data['quantity']
        productoption = ProductOption.objects.get(id=OrderItem.productoption_id)
        stockcount = productoption.stock_count
        stockcount = stockcount - quantity
        ProductOption.objects.filter(id=OrderItem.productoption_id).update(stock_count=stockcount)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        OrderItem = self.get_object(pk)
        OrderItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 관리자용 주문목록
class OrderedItemListAPIView(APIView):
    def get(self, request):
        qs = OrderItem.objects.filter(product__author=request.user)
        # qs2 = Product.objects.all().filter(author=request.user)
        # qs3 = OrderItem.objects.select_related('product')
        serializer = OrderItemSerializer(qs, many=True)
        return Response(serializer.data)


class OrderItemDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(OrderItem, pk=pk)

    def get(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = CartItemSerializer(OrderItem)
        return Response(serializer.data)
