from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import LoginForm


# Create your views here.
def sign_up(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            auth.login(request, new_user)
            return redirect('goods:index')
        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    context['form'] = LoginForm()
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
                auth.login(request, user)
                return redirect('goods:index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'
    context['form'] = LoginForm()
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('goods:index')
