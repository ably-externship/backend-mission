from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic import View


from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect("../main")
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
            return redirect("../main")
        # 아이디 or 비밀번호 오류
        else:
            return render(
                request, "login.html", {"error": "username or password is incorrect."}
            )

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("../main")


def kakao(request):
    return render(request, "kakao.html")


class KakaoSignInView(View):
    def get(self, request):
        app_key = KAKAO_REST_API_KEY
        redirect_uri = "http://localhost:8000/accounts/kakao/login/callback"
        kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        return redirect(
            f"{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}"
        )
