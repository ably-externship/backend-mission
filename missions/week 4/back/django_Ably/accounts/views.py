from os import access
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from requests.api import request
from rest_framework import permissions, response
from .models import AuthUser
from cart.models import Cart
from django.shortcuts import render, redirect
import datetime
import requests
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken

# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = AuthUser.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            is_active = 1,
                                            date_joined = datetime.datetime.now())
            # print(user.id)
            # cart = Cart.objects.create(auth_user=user)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    print(AuthUser.objects.filter(is_superuser=True))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = RefreshToken.for_user(user).access_token
            print(refresh, '/////////////', access)
            if username == '1234':
                response = redirect('/redstore/items/')
            else:
                response = redirect('/')
            response.set_cookie(key='token',value=access)
            print(response)
            auth.login(request, user)
    
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def token_on_header(request):
    access_token = 'Bearer ' + request.COOKIES['token']
    headers = {'Authorization': access_token}
    response = requests.get('http://127.0.0.1:8000/items/', headers=headers)
    return render(request, 'red_store_items.html', {'data':response.json()})



# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')

# home
def home(request):
    return render(request, 'home.html')
