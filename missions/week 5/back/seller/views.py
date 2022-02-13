from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from.serializers import *
from .models import Seller

# MTV로 셀러 등록하기 ---
def register(request):
    if request.method == 'POST':
        if Seller.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('/')
        else:
            market = request.POST['market']
            seller = Seller()
            seller.user = request.user
            seller.market = market
            seller.save()
            return HttpResponseRedirect('/')
    return render(request, 'seller/register.html', {})


# 셀러 토큰 ---
class SellerTokenObtainPairView(TokenObtainPairView):
    serializer_class = SellerTokenObtainPairSerializer


# 셀러 등록 ---
class SellerAccount(APIView):
    def get(self, request):
        try:
            instance = Seller.objects.get(user_id=request.user.id)
            serializer = SellerSerializer(instance)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        try:
            instance = Seller.objects.create(user=request.user)
            serializer = SellerSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            instance = Seller.objects.get(user_id=request.user.id)
            serializer = SellerSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            instance = Seller.objects.get(user_id=request.user.id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 셀러 상품 리스팅/등록 ---
class SellerProduct(APIView):
    def get_obj(self, request):
        seller = Seller.objects.get(user_id=request.user.id)
        return seller

    def get(self, request):
        try:
            instance = Product.objects.filter(seller_id=self.get_obj(request).id)
            serializer = ProductSerializer(instance, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        instance = Product.objects.create(seller_id=self.get_obj(request).id)
        serializer = ProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 셀러 상품 수정 및 삭제 ---
class SellerProductEdit(APIView):
    def get_obj(self, request, product_id):
        current_seller = Seller.objects.get(user_id=request.user.id)
        product = Product.objects.get(pk=product_id)
        if current_seller == product.seller:
            return product

    def get(self, request, product_id):
        try:
            instance = self.get_obj(request, product_id)
            serializer = ProductSerializer(instance)
            return Response(serializer.data)
        except:
             return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, product_id):
        try:
            instance = self.get_obj(request, product_id)
            serializer = ProductSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        try:
            instance = self.get_obj(request, product_id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 셀러 상품 옵션 등록 ---
class SellerProductOption(APIView):
    # 현재 로그인한 셀러의 상품이 맞는지 확인 후 상품 리턴
    def get_obj(self, request, product_id):
        current_seller = Seller.objects.get(user_id=request.user.id)
        product = Product.objects.get(pk=product_id)
        if current_seller == product.seller:
            return product

    def get(self, request, product_id):
        try:
            instance = Inventory.objects.filter(product_id=self.get_obj(request, product_id).id)
            serializer = InventorySerializer(instance, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, product_id):
        instance = Inventory.objects.create(product_id=self.get_obj(request, product_id).id)
        serializer = InventorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 셀러 상품 옵션 수정 및 삭제 ---
class SellerProductOptionEdit(APIView):
    # 현재 로그인한 셀러의 상품이 맞는지 확인
    def is_valid(self, request, product_id):
        current_seller = Seller.objects.get(user_id=request.user.id)
        product = Product.objects.get(pk=product_id)
        if current_seller == product.seller:
            return True
        return False

    def get(self, request, product_id, inventory_id):
        try:
            if self.is_valid(request, product_id) == True:
                instance = Inventory.objects.get(pk=inventory_id)
                serializer = InventorySerializer(instance)
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, product_id, inventory_id):
        try:
            if self.is_valid(request, product_id) == True:
                instance = Inventory.objects.get(id=inventory_id)
                serializer = InventorySerializer(instance, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, inventory_id):
        try:
            if self.is_valid(request, product_id) == True:
                instance = Inventory.objects.get(id=inventory_id)
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
