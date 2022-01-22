import os
import requests
from django.shortcuts import redirect, reverse, render
from django.contrib import messages, auth
from django.db.utils import IntegrityError
from .exception import *

from django.conf import settings
from accounts.models import User
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from django.core.exceptions import ObjectDoesNotExist
from dj_rest_auth.registration.views import SocialLoginView


DEBUG = bool(os.environ.get("DEBUG"))

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('login_page')
            
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def signup(request):
    if request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            user = User.objects.create_user(
                username=request.POST.get("username"), 
                email=request.POST.get("email"),
                password=request.POST.get("password1")
            )
            try:
                user.save()

                username=request.POST.get("username")
                auth.login(request, user)
                messages.success(request, f'반갑습니다, {username} 가입이 완료되었습니다.')
                return redirect('login_page')       
            except IntegrityError:
                messages.error(request, "User already exists")
                return redirect(reverse("signup"))

        else : 
            return render(request, 'signup.html', {'error' : '가입에 실패하였습니다'})
    return render(request, 'signup.html')


#-------------------------------------------------------------------------------------------------
def kakao_login(request):
    rest_api_key = 'ac6ad95e02f0b1a4e2b50b7fdf23e329'
    KAKAO_CALLBACK_URI = "http://127.0.0.1:8000/accounts/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )

def kakao_callback(request):
    # rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    rest_api_key = 'ac6ad95e02f0b1a4e2b50b7fdf23e329'
    BASE_URL = 'http://127.0.0.1:8000/'
    code = request.GET.get("code")
    KAKAO_CALLBACK_URI = "http://127.0.0.1:8000/accounts/kakao/callback/"
    redirect_uri = KAKAO_CALLBACK_URI
    """
    Access Token Request
    """
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    """
    Email Request
    """
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    kakao_account = profile_json.get('kakao_account')
    """
    kakao_account에서 이메일 외에
    카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
    print(kakao_account) 참고
    """
    print(kakao_account)
    try:
        email = kakao_account.get("email", None)
        try :
            user = User.objects.get(email=email)
        except User.DoesNotExist :
            user = None

        if user is not None:
            KakaoException( "이미 가입된 user 입니다.")

        else:
            user = User.objects.create_user(
                email=email,
                username=email,
            )

            user.set_unusable_password()
            user.save()
        
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, f"{user.email} signed up and logged in with Kakao")
        return redirect(reverse("main_page"))

    except KakaoException as error:
        messages.error(request, error)
        return redirect(reverse("main_page"))
    except LoggedOutOnlyFunctionView as error:
        messages.error(request, error)
        return redirect(reverse("home_page"))



class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    KAKAO_CALLBACK_URI = "http://127.0.0.1:8000/accounts/kakao/callback/"
    callback_url = KAKAO_CALLBACK_URI


def check_email(request):
    return render(request, "check_email.html")


