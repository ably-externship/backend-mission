from lib2to3.pgen2 import token
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View


from user.forms import UserForm

from cart.models import Cart
from .models import User


import os
import requests
import json

from project.settings import BASE_DIR

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserForm()

    return render(request, 'user/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


class KakaoSignInView(View):

    def get(self, request):
        api_key = secrets["REST_API_KEY"]
        redirect_uri = 'http://127.0.0.1:8000/users/login/kakao/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'

        return redirect(
            f'{kakao_auth_api}&client_id={api_key}&redirect_uri={redirect_uri}'
        )


class KakaoSignInCallBackView(View):
    def get(self, request):
        auth_code = request.GET.get('code')
        client_id = secrets["REST_API_KEY"]
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'redirect_uri': 'http://127.0.0.1:8000/users/login/kakao/callback',
            'code': auth_code,
            'client_secret': secrets["CLIENT_SECRET"]
        }

        token_response = requests.post(kakao_token_api, data=data)

        access_token = token_response.json().get('access_token')

        user_info_response = requests.get(
            'https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})

        user_info_response = user_info_response.json()

        kakao_account = user_info_response.get("kakao_account")
        profile = kakao_account.get("profile")

        nickname = profile.get("nickname", None)
        email = kakao_account.get("email", None)

        user = User.objects.get_or_none(email=email)
        if user is None:
            user = User.objects.create_user(username=nickname, email=email)
            user.set_unusable_password()
            user.save()
            cart = Cart.objects.create(user=user)
            cart.save()

        auth_login(request, user)

        return redirect('product:index')
