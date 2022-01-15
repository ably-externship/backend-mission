import json
import requests

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from base.settings.common import KAKAO_OAUTH_CONFIG
from users.forms import CustomAuthenticationForm
from users.models import User


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/product')
    return render(request, 'auth/login.html', {'form': CustomAuthenticationForm})


def logout_call(request):
    logout(request)
    return redirect('/auth/login')


def sign_up(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        User.objects.create_user(username=email, email='', password=password1, name=name)
        return redirect('/auth/login')
    return render(request, 'auth/sign_up.html', {'form': UserCreationForm})


def email_duplicate_check(request):
    username = request.GET['username']
    try:
        User.objects.get(username=username)
        return JsonResponse({'data': False})
    except User.DoesNotExist:
        return JsonResponse({'data': True})


@csrf_exempt
def find_id(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            user = User.objects.get(name=name)
            return JsonResponse({'data': user.username})
        except User.DoesNotExist:
            return JsonResponse({'data': False})
    return render(request, 'auth/find_id.html')


@csrf_exempt
def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
            reset_password = get_random_string(length=10)
            email = EmailMessage('패스워드 초기화 안내'
                                 , '회원님의 초기화 패스워드는 ' + reset_password + '입니다'
                                 , 'v49011591@gmail.com'
                                 , [user.username])
            email.send()
            user.set_password(reset_password)
            user.save()
            return JsonResponse({'data': user.username})
        except User.DoesNotExist:
            return JsonResponse({'data': False})
    return render(request, 'auth/password_reset.html')


def kakao_sign_view(request):
    app_key = KAKAO_OAUTH_CONFIG['KAKAO_REST_API_KEY']
    redirect_uri = KAKAO_OAUTH_CONFIG['KAKAO_REDIRECT_URI']
    kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
    return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}')


def kakao_login_callback(request):
    if request.method == 'GET':
        code = request.GET['code']
        app_key = KAKAO_OAUTH_CONFIG['KAKAO_REST_API_KEY']
        redirect_uri = KAKAO_OAUTH_CONFIG['KAKAO_REDIRECT_URI']
        token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': app_key,
            'redirection_uri': redirect_uri,
            'code': code
        }

        token_response = requests.post(token_api, data=data)

        access_token = token_response.json().get('access_token')

        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer ${access_token}'})
        user_info = user_info_response.json()

        id = user_info.get("id")

        try:
            user = User.objects.get(username=id)
            login(request, user)
            return redirect('/product')
        except User.DoesNotExist:
            user = User.objects.create_user(username=id)
            login(request, user)
            return redirect('/product')

