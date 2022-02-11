from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.api.permission import IsSeller, IsAuthor
from product.api.serializers import ProductSerializer, CartItemSerializer, \
    OrderItemSerializer, CartItemOrderSerializer
from rest_framework.pagination import PageNumberPagination
from product.models import Product, CartItem, OrderItem, ProductOption


class PageNumberPagination(PageNumberPagination):
    page_size = 10


# 상품 조회 및 삭제
class ProductListView(APIView):
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


class ProductDetailView(APIView):
    pagination_class = PageNumberPagination
    permission_classes = [IsSeller]

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


# 장바구니 추가 및 조회
class CartItemListView(APIView):
    def get(self, request):
        qs = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = self.request.user.id
        product_id = request.data['product_id']
        product_option_id = request.data['product_option_id']

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id, product_id=product_id, product_option_id=product_option_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CartItemDetailView(APIView):
    permission_classes = [IsAuthor]

    def get_object(self, pk):
        try:
            qs = CartItem.objects.get(pk=pk)
            self.check_object_permissions(self.request, qs)
            return qs
        except ObjectDoesNotExist:
            return None

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


# 장바구니 상품 주문
class CartItemOrderView(APIView):
    def post(self, request):
        for order in request.data['orders']:
            user_id = order['user_id']
            product_id = order['product_id']
            product_option_id = order['product_option_id']
            # quantity = order['quantity']

            serializer = CartItemSerializer(data=request.data)

            if serializer.is_valid():
                breakpoint()
                serializer.save(user_id, product_id, product_option_id)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)


# 주문하기 및 주문 목록 조회
class OrderItemListView(APIView):
    def get(self, request):
        qs = OrderItem.objects.filter(user=request.user)
        serializer = OrderItemSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        product_option_id = request.data['product_option_id']
        serializer = OrderItemSerializer(data=request.data)
        productoption = ProductOption.objects.get(id=product_option_id)
        stockcount = productoption.stock_count
        stockcount -= 1
        ProductOption.objects.filter(id=product_option_id).update(stock_count=stockcount)

        if serializer.is_valid():
            serializer.save(user_id=user_id, product_id=product_id, product_option_id=product_option_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderItemDetailView(APIView):
    permission_classes = [IsAuthor]

    def get_object(self, pk):
        try:
            qs = CartItem.objects.get(pk=pk)
            self.check_object_permissions(self.request, qs)
            return qs
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = OrderItemSerializer(OrderItem)
        return Response(serializer.data)

    def patch(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = OrderItemSerializer(OrderItem, data=request.data, partial=True)
        quantity = request.data['quantity']
        productoption = ProductOption.objects.get(id=OrderItem.product_option_id)
        stockcount = productoption.stock_count
        stockcount = stockcount - quantity
        ProductOption.objects.filter(id=OrderItem.product_option_id).update(stock_count=stockcount)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        OrderItem = self.get_object(pk)
        OrderItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 관리자용 주문목록
class OrderedItemListView(APIView):
    def get(self, request):
        qs = OrderItem.objects.filter(product__author=request.user)
        # qs2 = Product.objects.all().filter(author=request.user)
        # qs3 = OrderItem.objects.select_related('product')
        serializer = OrderItemSerializer(qs, many=True)
        return Response(serializer.data)


class OrderedItemDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(OrderItem, pk=pk)

    def get(self, request, pk):
        OrderItem = self.get_object(pk)
        serializer = CartItemSerializer(OrderItem)
        return Response(serializer.data)
