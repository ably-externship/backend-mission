from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from market.models import Market
from product.models import Product
from ..models import ProductDailySales,MarketDailySales
from .serializers import MarketDailySalesSerializer,ProductDailySalesSerializer

class ProductDailyList(APIView):
    """
    상품전체 일일매출
    """

    permission_classes = [IsAdminUser,]

    def get(self,request):
        print('whatetete')
        product = ProductDailySales.objects.all()
        serializers = ProductDailySalesSerializer(product,many=True)
        return Response(serializers.data)


class ProductDailyDetail(APIView):
    """
    상품별 일일매출
    """
    permission_classes = [IsAdminUser,]
    
    def get(self,request,product_id):
        date = request.data['date']
        product = Product.objects.get(pk=product_id)
        products = ProductDailySales.objects.filter(product=product)
        serializer = ProductDailySalesSerializer(products,many=True)
        return Response(serializer.data)


class MarketDailyList(APIView):
    """
    마켓전체 일일매출
    """

    permission_classes = [IsAdminUser,]

    def get(self,request):
        market = MarketDailySales.objects.all()
        serializers = MarketDailySalesSerializer(data=market,many=True)
        return Response(serializers.data)
class MarketDailyDetail(APIView):
    """
    마켓별 일일매출
    """
    permission_classes = [IsAdminUser,]
    
    def get(self,request,market_id):
        date = request.data['date']
        market = Market.objects.get(pk=market_id)
        market_sales = MarketDailySales.objects.filter(market=market)
        serializers = ProductDailySalesSerializer(data=market_sales,many=True)
        return Response(serializers.data)



