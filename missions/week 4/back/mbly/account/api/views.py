from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from market.models import Market

class UserInfoView(APIView):
    """
    사용자 정보 출력
    """
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = User.objects.get(pk = request.user.id)
        market = Market.objects.filter(master = user)
        serializer = UserSerializer(user)
        return Response(serializer.data)