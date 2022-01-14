from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import *
from .forms import *


def signup(request):
    if request.method == "POST":
        id = request.POST["id"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        join = User(
            id=id,
            username=username,
            password1=password1,
            password2=password2,
            email=email,
        )
        join.save()
        return redirect("/")
    else:
        boardForm = BoardForm
        join = User.objects.all()
        context = {
            "boardForm": boardForm,
            "board": join,
        }
        return render(request, "signup.html", context)


def login(request):
    if request.method == "POST":
        id = request.POST["id"]
        password1 = request.POST["password1"]
        user = auth.authenticate(request, id=id, password1=password1)

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


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect("")
    return render(request, "login.html")
