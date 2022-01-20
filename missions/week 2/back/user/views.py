from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from argon2 import PasswordHasher, exceptions
from .forms import SignupForm
from .models import User

# 카카오 로그인시 필요한 모듈
import requests
import secrets
from config.settings import KAKAO_KEY, kakao_redirect_uri


class SignupView(FormView):
    template_name = "user/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('user:result')

    def form_valid(self, form):
        user_name = form.cleaned_data.get("user_name")
        user_id = form.cleaned_data.get("user_id")
        user_pw = form.cleaned_data.get("user_pw")
        user_email = form.cleaned_data.get("user_email")
        user = User.objects.create(user_name=user_name,
                                   user_id=user_id,
                                   user_pw=PasswordHasher().hash(user_pw),
                                   user_email=user_email)
        user.save()
        return super().form_valid(form)


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        try:
            user = User.objects.get(user_id=user_id)
            if PasswordHasher().verify(user.user_pw, user_pw):  # db에 저장된 암호와 로그인 입력된 암호 검증
                request.session['user'] = user.user_id
                request.session['user_name'] = user.user_name
                return redirect('product:main')
            # return JsonResponse({"message": "Login Success"}, status=200)

        except (User.DoesNotExist, exceptions.VerifyMismatchError):
            return redirect('user:login')

    else:
        return render(request, "user/login.html")


def logout(request):
    if 'is_kakao' in request.session:
        url = "https://kapi.kakao.com/v1/user/logout"
        headers = {
            "Authorization": "Bearer " + request.session['token']
        }

        requests.post(url, headers=headers)
        request.session.pop('is_kakao')
        request.session.pop('token')

    request.session.pop('user')
    if "user_name" in request.session:
        request.session.pop('user_name')
    return redirect('product:main')


def result(request):
    return render(request, 'user/success.html')


# 카카오 로그인
def kakao_connect(request):
    """카카오 소셜 로그인을 위한 인가 코드 받기"""
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_KEY}&redirect_uri={kakao_redirect_uri}&response_type=code'
    response = redirect(url)
    return response


def KakaoLogin(request):
    """인가 코드를 이용하여 사용자 액세스 토큰 받아오고 로그인 기능 구현 """
    code = request.GET.get('code')
    error = request.GET.get('error')
    # error_description = request.GET.get('error_description')
    # 카카오 로그인 관련 오류 처리
    if error:
        context = {
            'message': '인증 실패, 다시 시도해주십시오.'
        }
        return render(request, 'user/login.html', context=context)

    # 사용자 액세스 토큰 받기
    url = f'https://kauth.kakao.com/oauth/token'
    headers = {
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_KEY,
        "redirect_uri": kakao_redirect_uri,
        "code": code,
    }

    res = requests.post(url, headers=headers, data=data)
    token_type = res.json()['token_type']
    access_token = res.json()['access_token']

    # 사용자 정보 받아오기
    url = "https://kapi.kakao.com/v2/user/me"
    headers = {
        "Authorization": token_type + " " + access_token,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    res = requests.get(url, headers=headers)
    res = res.json()
    user_id = res["id"]
    nickname = res["properties"]["nickname"]

    # 받아온 정보로 회원 여부 확인하고 없을시 가입 후 로그인
    try:
        user = User.objects.get(user_id=user_id)

    except User.DoesNotExist:
        user = User(user_id=user_id,
                    user_name=nickname,
                    user_pw=secrets.token_bytes(),
                    user_email="default@default.com",
                    is_social=True)
        user.save()

    request.session['token'] = access_token
    request.session['user'] = user.user_id
    request.session['user_name'] = user.user_name
    request.session['is_kakao'] = True

    return redirect('product:main')


