from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Lionuser
from .serializers import LionuserSerializer, UserSerializer, UserLoginSerializer, LionuserLoginSerializer
# Create your views here.

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, authenticate

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def loginTest(request):
    if request.method == 'GET':
        return JsonResponse({"Success": "header에 jwt token으로 api 요청 성공"})


from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'authuser post error'})
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'message': 'your auth data post lionuser created'})


class LoginUser(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 로그인 에러입니다.'})

        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 존재하지 않습니다.'})
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user == None:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '비밀번호가 틀렸습니다.'})

        refresh = RefreshToken.for_user(user)
        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'message': 'your auth data post lionuser 로그인'})


# from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

#Custom
class LionUserAPI(APIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        lions = Lionuser.objects.all();
        serializer = LionuserSerializer(lions, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        print(request.data)
        serializer = LionuserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'auth custom lion user post error'})
        serializer.save()

        user = Lionuser.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'message': 'your auth data post lionuser created'})

#<pk> put, retrieve, delete



class LionLoginUser(APIView):
    def post(self, request):
        serializer = LionuserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 로그인 에러입니다.'})

        try:
            user = Lionuser.objects.get(username=request.data['username'])
        except Lionuser.DoesNotExist:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 존재하지 않습니다.'})
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user == None:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '비밀번호가 틀렸습니다.'})

        refresh = RefreshToken.for_user(user)
        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'message': 'your auth data post lion custom user 로그인'})
