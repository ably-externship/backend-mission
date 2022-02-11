from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import UserForm
# Create your views here.
from mbly.settings import SOCIAL_OUTH_CONFIG
import requests
import json
from django.contrib.auth.models import User


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

def kakao_login(request):
    """
    카카오 로그인
    """
    API_KEY = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URI = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    return redirect( f'https://kauth.kakao.com/oauth/authorize?client_id={API_KEY}&redirect_uri={REDIRET_URI}&response_type=code')
    

def kakao_callback(request):
    """
    카카오 콜백
    """
    code = request.GET['code']
    API_KEY = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URI = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']


    url = 'https://kauth.kakao.com/oauth/token'
    headers = {'Content-type':'application/x-www-form-urlencoded; charset=utf-8'}

    body = {'grant_type' : 'authorization_code',
    'client_id':API_KEY,
    'redirect_uri':REDIRET_URI,
    'code':code}

    token_kakao_response = requests.post(url,headers=headers,data=body)


    access_token = json.loads(token_kakao_response.text).get('access_token')
    url = "https://kapi.kakao.com/v2/user/me" # Authorization(프론트에서 받은 토큰)을 이용해서 회원의 정보를 확인하기 위한 카카오 API 주소
    headers      ={
        'Authorization' : f"Bearer {access_token}"}

    kakao_response = requests.get(url,headers=headers)
    kakao_response = json.loads(kakao_response.text)
    print(kakao_response)
    email = kakao_response['kakao_account']['email']
    isexist = User.objects.filter(email =email ).exists()
    if isexist:
        # email 존재
        user = User.objects.filter(email=email).first()
        login(request,user)
    else:
        # 존재 X
        new_user = User(
            username = 'kakao_'+str(kakao_response['id']),
            email = email
        )
        new_user.save()
        login(request, new_user)  # 로그인
    return redirect('/')
        

    