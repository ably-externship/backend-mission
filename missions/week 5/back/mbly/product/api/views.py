from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ..models import Product, RealProduct
from .serializers import ProductSerializer,RealProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,AllowAny
from market.models import Market
class ProductList(ListCreateAPIView):
    """
    상품 리스트, 생성
    get,post
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """
    마켓명 detail
    get,update,delete
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

class ProductMarketList(APIView):
    """
    마켓별 상품
    """
    permission_classes = [IsAdminUser]
    def get(self,request):
        market = Market.objects.get(master = request.user)
        products = Product.objects.filter(market = market )
        serializer = ProductSerializer(products,many= True)
        return Response(serializer.data)
    
    def post(self,request):
        market = Market.objects.get(master = request.user)
        # request.data['market']=market
        print(request.data)
        serializer = ProductSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save(market = market)
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status=400)

class ProductMarketDetail(APIView):
    """
    마켓별 상품 detail
    """
    permission_classes = [IsAdminUser,]
    def patch(self,request,product_id):
        market = Market.objects.get(master = request.user)
        product = Product.objects.get(pk = product_id)
        if product.market == market:
            request.data['market'] = market
            print(request.data)
            serializer = ProductSerializer(data = request.data , instance=product)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status= 200)
            return Response(serializer.errors,status = 400)
        return Response({"message": "상품마켓과 다릅니다."},status = 401)
    
    def delete(self,request,product_id):
        print(product_id)
        market = Market.objects.get(master = request.user)
        product = Product.objects.get(pk = product_id)
        if product.market == market:
            product.delete()
            return Response({"message":"Product deleted"})
        return Response({"messages" : "different market"})


class RealProductList(APIView):
    """
    상품 Option 리스트, 생성
    get,post
    """
    permission_classes = [IsAdminUser,]
    def post(self,request):
        product_id = request.data['product_id']
        product = Product.objects.get(pk = product_id)
        
        if product.market.master == request.user:
            serializer = RealProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(product = product)
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"message":"상품 마켓과 다릅니다."},status = 400)

    def get(self,request):
        product_id = request.data['product_id']
        product = Product.objects.get(pk = product_id)
        print(product)
        if product.market.master == request.user:
            realproducts = RealProduct.objects.filter(product=product)
            serializer = RealProductSerializer(realproducts,many= True)
            return Response(serializer.data)
        return Response({"message":"상품 마켓과 다릅니다."},status = 400)

class RealProductDetail(APIView):
    """
    마켓별 상품 detail
    """
    permission_classes = [IsAdminUser]
    def patch(self,request,option_id):
        product_id = request.data["product_id"]
        market = Market.objects.get(master = request.user)
        product = Product.objects.get(pk = product_id)
        if product.market == market:
            request.data['market'] = market
            print(request.data)
            serializer = ProductSerializer(data = request.data , instance=product)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status= 200)
            return Response(serializer.errors,status = 400)
        return Response({"message": "상품마켓과 다릅니다."},status = 401)
    
    def delete(self,request,option_id):
        # product_id = request.data["product_id"]

        market = Market.objects.get(master = request.user)
        option = RealProduct.objects.get(pk = option_id)


        product = option.product
        if product.market == market:
            product.delete()
            return Response({"message":"Product deleted"})
        return Response({"message": "상품마켓과 다릅니다."},status = 401)