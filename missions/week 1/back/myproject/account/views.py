from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *


@csrf_exempt
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect("../")
        return render(request, "signup.html")
    return render(request, "signup.html")


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        # 로그인 성공
        if user is not None:
            auth.login(request, user)
            return redirect("")
        # 아이디 or 비밀번호 오류
        else:
            return render(
                request, "login.html", {"error": "username or password is incorrect."}
            )

    else:
        return render(request, "login.html")


@csrf_exempt
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect("")
    return render(request, "login.html")
