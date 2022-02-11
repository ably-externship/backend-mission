from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpRequest
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status, generics
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User






@api_view(['GET'])
def current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer



class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("에러 코드 :", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ApiRefreshRefreshTokenView(GenericAPIView):
#     permission_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.
#     authentication_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.
#
#     serializer_class = ApiRefreshRefreshTokenSerializer
#
#     # 리프레시 토큰 자체를 다시 발급
#     def post(self, request: HttpRequest):
#         serializer: ApiRefreshRefreshTokenSerializer = self.get_serializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#
#         refresh: str = serializer.validated_data['refresh']
#
#         try:
#             refresh_token: RefreshToken = RefreshToken(refresh)
#         except TokenError as e:
#             raise InvalidToken(e)
#
#         user: User = get_object_or_404(User, id=refresh_token['user_id'])
#         new_refresh_token = MyTokenObtainPairSerializer.get_token(user)  # 이걸로 토큰을 생성해야 합니다. 다른 방법으로 하면 페이로드에 필수데이터가 누락된 버전이 생김
#         new_access_token = new_refresh_token.access_token
#         refresh_token.blacklist()  # 꼭 블랙리스트에 넣어주세요.
#
#         return Response({
#             'refresh': str(new_refresh_token),
#             'access': str(new_access_token),
#         })