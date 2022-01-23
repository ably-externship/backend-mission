from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from.serializers import ProductSerializer, InventorySerializer, CustomTokenObtainPairSerializer
from shop.models import Product, Inventory


# 상품 목록 ---
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 개별 상품  ---
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, pk):
        instance = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# 상품 옵션 ---
class InventoryCreate(APIView):
      def get(self, request, product_id):
        instance = Inventory.objects.filter(product_id=product_id)
        serializer = InventorySerializer(instance, many=True)
        return Response(serializer.data)

      def post(self, request, product_id):
        instance = Inventory.objects.create(product_id=product_id)
        serializer = InventorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductInventory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "pk"

    def put(self, request, pk):
        instance = Inventory.objects.get(pk=pk)
        serializer = InventorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 토큰 ---
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class BlacklistTokenUpdateView(APIView):
    authentication_classes = ()
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)