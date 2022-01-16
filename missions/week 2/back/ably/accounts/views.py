from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.conf import settings
from .models import User
from django.contrib import auth
import requests


# Create your views here.
def sign_up(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            username = request.POST['username']

            qs = User.objects.filter(username=username)
            if not qs.exists():
                new_user = User.objects.create_user(
                    username=username,
                    password=request.POST['password'],
                )

                auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('products:index')
            else:
                context['error'] = '아이디 중복'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # GET Method
    return render(request, 'accounts/sign_up.html', context)


def login(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:

            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password'],
            )

            if user is not None:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('products:index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # GET Method
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('products:index')


def kakao_login(request):
    rest_api_key = settings.REST_API_KEY
    redirect_uri = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    authorize_url = f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={rest_api_key}&redirect_uri={redirect_uri}'

    request.session['client_id'] = rest_api_key
    request.session['redirect_uri'] = redirect_uri

    return redirect(authorize_url)


def kakao_oauth(request):
    code = request.GET['code']

    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')

    token_url = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code,
    }

    response = requests.post(token_url, data=data)
    json_data = response.json()
    access_token = json_data['access_token']

    access_token_info_url = 'https://kapi.kakao.com/v2/user/me'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(access_token_info_url, headers=headers)
    json_data = response.json()
    id = json_data['id']
    username = json_data['kakao_account']['profile']['nickname']

    qs = User.objects.filter(id=id)
    if not qs.exists():
        new_user = User.objects.create_user(
            username=username,
            id=id,
            register_login_method='kakao',
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
    else:
        user: User = qs.first()
        if user.register_login_method != 'kakao':
            return redirect('accounts:login')
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return redirect('products:index')
