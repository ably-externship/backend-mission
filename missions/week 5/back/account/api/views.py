from django.contrib.auth import login, logout, authenticate
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from account.api.serializers import SignupUserSerializer, LoginSerializer
from account.models import User


class SignupUserView(APIView):
    def post(self, request):
        serializer = SignupUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        if User.objects.filter(username=username).exists():
            return Response(data={'error': '이미 존재하는 username 입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        User.objects.create_user(username=username, email=serializer.validated_data['email'],
                                 password=serializer.validated_data['password'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):

        user = authenticate(username=request.data['username'], password=request.data['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)

