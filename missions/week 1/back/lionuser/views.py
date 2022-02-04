from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Lionuser
from .serializers import LionuserSerializer, UserSerializer, UserLoginSerializer, LionuserLoginSerializer
# Create your views here.

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, authenticate

import requests

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, ApiRefreshRefreshTokenSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

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
            print(f"User Email --> {request.user.email}") #payload
            print(f"User Id --> {request.user.id}")
            print(f"User --> {request.user}")

            print(f"User type --> {request.user.user_type}")
            print(f"User shop --> {request.user.shop}")
            print("---테스트성공---")

        else:
            print("User is not logged in :(")
            print("테스트실패!!!")

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
        refresh = RefreshToken.for_user(user) #토큰 발급시 payload
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



# 이걸 사용하는 이유는 JWT 토큰안의 페이로드 안에 추가적인 내용(email, profile_img_url 등)을 담기 위함
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#Custom 회원가입
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

        user: Lionuser = get_object_or_404(Lionuser, id=refresh['user_id'])
        # 이걸로 토큰을 생성해야 합니다. 다른 방법으로 하면 페이로드에 필수데이터가 누락된 버전이 생김
        new_refresh_token = MyTokenObtainPairSerializer.get_token(
            user)#
        new_access_token = new_refresh_token.access_token
        refresh.blacklist()  # 꼭 블랙리스트에 넣어주세요.

        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(new_refresh_token),
                         'access': str(new_access_token), 'message': 'your auth data post lionuser created'})

#Custom 로그인
class LionLoginUser(APIView):
    def post(self, request):
        print("로그인 시도!!!!!-----")
        serializer = LionuserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 로그인 에러입니다.'})

        try:
            user = Lionuser.objects.get(username=request.data['username'])
        except Lionuser.DoesNotExist:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '유저 존재하지 않습니다.'})
        user = authenticate(username=request.data['username'], password=request.data['password'])

        if user == None:
            return Response({'status': 403, 'errors': serializer.errors, 'message': '비밀번호가 틀렸습니다.'})

        refresh = RefreshToken.for_user(user)

        user: Lionuser = get_object_or_404(Lionuser, id=refresh['user_id'])
        # 이걸로 토큰을 생성해야 합니다. 다른 방법으로 하면 페이로드에 필수데이터가 누락된 버전이 생김
        new_refresh_token = MyTokenObtainPairSerializer.get_token(
            user)
        new_access_token = new_refresh_token.access_token
        refresh.blacklist()  # 꼭 블랙리스트에 넣어주세요.

        return Response({'status': 201, 'payload': serializer.data, 'refresh': str(new_refresh_token),
                         'access': str(new_access_token), 'message': 'your auth data post lion custom user 로그인'})



class KakaoSignInView(APIView):
    def get(self, request):
        app_key = "183b1738c1dcd7012baaf747c970ba3f"
        redirect_url = "http://localhost:8000/user/login/kakao"
        kakao_auth_api = "https://kauth.kakao.com/oauth/authorize"
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

    kakao_user_info = requests.post(kakao_user_url, headers=headers).json()

    #내 DB에 저장해서 jwt token발급
    print(kakao_user_info['properties']['nickname'])
    print(kakao_user_info['kakao_account']['email'])

    # TODO: 중복체크
    # user = Lionuser.objects.create(username=kakao_user_info['properties']['nickname'], email=kakao_user_info['kakao_account']['email']) #, first_name = "harim")
    # user.setType("카카오"), # TODO: 추후 사용자 DB에 provider_type 추가
    # user.save()

    user = Lionuser.objects.get(email=kakao_user_info['kakao_account']['email'])
    refresh = RefreshToken.for_user(user)

    #header에 넣어서 , 요청 my page
    print("jwt token")
    print(str(refresh.access_token))

    return redirect('/user/check',{'status': 201, 'payload': user.username, 'refresh': str(refresh),
                      'access': str(refresh.access_token), 'message': 'your kakao lionuser created'})

def checkJwt(request):
    print(request)
    print(request.method)
    print(request.body)

    return render(request, 'check_jwt.html')



# 엑세스키와 리프레시키를 모두 재발급하는 로직 custom
class ApiRefreshRefreshTokenView(GenericAPIView):
    permission_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.
    authentication_classes = ()  # 중요, 이렇게 해야 접근이 가능합니다.

    serializer_class = ApiRefreshRefreshTokenSerializer

    # 리프레시 토큰 자체를 다시 발급
    def post(self, request: HttpRequest):
        serializer: ApiRefreshRefreshTokenSerializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        refresh: str = serializer.validated_data['refresh']

        try:
            refresh_token: RefreshToken = RefreshToken(refresh)
        except TokenError as e:
            raise InvalidToken(e)

        user: Lionuser = get_object_or_404(Lionuser, id=refresh_token['user_id'])
        new_refresh_token = MyTokenObtainPairSerializer.get_token(user)  # 이걸로 토큰을 생성해야 합니다. 다른 방법으로 하면 페이로드에 필수데이터가 누락된 버전이 생김
        new_access_token = new_refresh_token.access_token
        refresh_token.blacklist()  # 꼭 블랙리스트에 넣어주세요.

        return Response({
            'refresh': str(new_refresh_token),
            'access': str(new_access_token),
        })
