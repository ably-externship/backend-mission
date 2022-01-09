from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def profile(request):
    return render(request, 'accounts/profile.html')


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
    User.objects.create_user(username=username, email=email, password=password1)
    return render(request, 'accounts/register_succeeded.html', {
        'username': username
    })


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
