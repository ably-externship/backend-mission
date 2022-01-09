from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signin (request):
    if request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['password']
        user = authenticate(username = id, password = pwd)
        if user is not None:
            login(request, user)
            return redirect('main')
        else :
            return HttpResponse('로그인 실패!')
    else :
        return render(request, 'accounts/login.html')

def signup (request):
    if request.method == 'POST':
        pwd = request.POST['pwd']
        pwdConf = request.POST['pwdConf']
        if pwd == pwdConf :
            id = request.POST['UserID']
            name = request.POST['name']
            email = request.POST['email']
            new_user = User.objects.create_user(username=id, password=pwd, email=email, first_name=name)
            login(request, new_user)
            return redirect('main')
        else :
            return redirect('signup')
    else :
        return render(request, 'accounts/signup.html')

@login_required
def mypage (request):
    return render(request, 'accounts/mypage.html')