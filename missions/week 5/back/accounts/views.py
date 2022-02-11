import requests
from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic

# Create your views here.
from accounts.decorators import logout_required
from base.settings.common import KAKAO_REST_API_KEY


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'accounts/profile.html'


@logout_required
def register(request):
    class RegisterForm(UserCreationForm):
        email = forms.EmailField()

    return render(request, 'accounts/register.html', {
        'form': RegisterForm()
    })


def register_succeeded(request):
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if password1 != password2:
        return HttpResponse('Passwords do not match.')
    user = get_user_model().objects.create_user(username=username, email=email, password=password1)
    login(request, user)
    return render(request, 'accounts/register_succeeded.html', {
        'username': username
    })


@logout_required
def recovery(request):
    class RecoveryForm(forms.Form):
        email = forms.EmailField()

    return render(request, 'accounts/recovery.html', {
        'form': RecoveryForm()
    })


def recovery_done(request):
    email = request.POST['email']
    try:
        user = get_user_model().objects.get(email=email)
        send_mail(
            '[멋블리] 아이디 찾기 결과',
            f'{user.username}',
            'noreply@mbly.o-r.cc',
            [email]
        )
        return HttpResponse('이메일로 아이디를 보내드렸습니다.')
    except get_user_model().DoesNotExist:
        return HttpResponse('아이디를 찾을 수 없습니다.')


@logout_required
def kakao_login(request):
    host = 'https://mbly.o-r.cc'
    client_id = KAKAO_REST_API_KEY
    redirect_uri = f'{host}/accounts/login/kakao/callback'
    return redirect(
        f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code')


def kakao_login_callback(request):
    host = 'https://mbly.o-r.cc'
    code = request.GET.get('code')
    client_id = KAKAO_REST_API_KEY
    redirect_uri = f'{host}/accounts/login/kakao/callback'
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code
    }
    token = requests.post('https://kauth.kakao.com/oauth/token', data=data).json()
    # 사용자 정보 조회
    kakao_profile = requests.get('https://kapi.kakao.com/v2/user/me', headers={
        'Authorization': 'Bearer ' + token['access_token'],
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }).json()
    get_user_model().login_with_kakao(request, kakao_profile)
    return redirect(reverse('profile'))
