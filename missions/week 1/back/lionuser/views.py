from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Lionuser
from .serializers import LionuserSerializer, UserSerializer, UserLoginSerializer, LionuserLoginSerializer
# Create your views here.

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, authenticate

import requests


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
    print("테스트 시도!!!1")
    if request.method == 'GET':
        if request.user.is_authenticated:
            print("User is logged in :)")
            print(f"Username --> {request.user.username}")
            print("테스트성공")

        else:
            print("User is not logged in :(")
            print("테스트실패!!")

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
        print(refresh)
        print(str(refresh.access_token))
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
        print("로그인 시도!!!!----------------")
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



class KakaoSignInView(APIView):
    def get(self, request):
        app_key = APP_KEY
        redirect_url = "http://localhost:8000/user/login/kakao"
        kakao_auth_api = "https://kauth.kakao.com/oauth/authorize"
        print(f'{kakao_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_url}')

        return redirect(f'{kakao_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_url}')

def kakaoTest(request):
    #DB error -> custom user

    # accessToken 받기
    # access token
    k_access_token = str(request.GET.get('code', None))
    print(k_access_token)

    app_key = "183b1738c1dcd7012baaf747c970ba3f"
    redirect_url = "http://localhost:8000/user/login/kakao"
    kakao_auth_token_api = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    client_secret = "saNjsXd1W6G7YwAjMJf5JKbjsayDJzkY"
    print(f'{kakao_auth_token_api}client_id={app_key}&redirect_uri={redirect_url}&code={k_access_token}&client_secret={client_secret}')
    url_k = f'{kakao_auth_token_api}client_id={app_key}&redirect_uri={redirect_url}&code={k_access_token}&client_secret={client_secret}'
    response = requests.post(url_k)
    print(response.status_code)
    print(response.content)
    print(response.json())
    print(response.json()['access_token'])

    access_token = response.json()['access_token']
    #사용자 정보 가져오기
    kakao_user_url = "https://kapi.kakao.com/v2/user/me"

    headers = {"Authorization": f"Bearer {access_token}"}
    print(headers)
    print(headers)

    kakao_user_info = requests.post(kakao_user_url, headers=headers).json()

    #내 DB에 저장해서 jwt token발급
    print(kakao_user_info['properties']['nickname'])
    print(kakao_user_info['kakao_account']['email'])

    #TODO: 중복체크
    #user = Lionuser.objects.create(username=kakao_user_info['properties']['nickname'], email=kakao_user_info['kakao_account']['email']) #, first_name = "harim")
    # #user.setType("카카오"), #TODO: 추후 사용자DB에 type 추가
    # user.save()
    #
    user = Lionuser.objects.get(email=kakao_user_info['kakao_account']['email']) #
    refresh = RefreshToken.for_user(user)
    #if request.method == 'GET':

    #header에 넣어서 , 요청 mypage
    print("jwt token")
    print(str(refresh.access_token))


    return redirect('/user/check',{'status': 201, 'payload': user.username, 'refresh': str(refresh),
                      'access': str(refresh.access_token), 'message': 'your kakao lionuser created'})
    return render(request, 'product_detail.html', {'product': product})

def checkJwt(request):
    print(request)
    print(request.method)
    print(request.body)


    #decode해서 mypage



    return render(request, 'check_jwt.html')
