from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ..models import Market
from .serializers import MarketSerializer




class MarketList(ListCreateAPIView):
    """
    마켓명 리스트, 생성
    get,post
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketDetail(RetrieveUpdateDestroyAPIView):
    """"
    마켓명 detail
    get,put,update
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


