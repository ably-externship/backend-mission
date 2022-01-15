import requests
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from config.settings import env
from accounts.models import User
from .forms import LoginForm, SignupForm


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class KakaoException(Exception):
    pass


def kakao_login(request):
    kakao_key = env('KAKAO_KEY')
    redirect_uri = env('REDIRECT_URI')
    # redirect_uri = 'http://127.0.0.1:8000/users/login/kakao/callback'
    host = 'https://kauth.kakao.com'
    url = f'/oauth/authorize?client_id={kakao_key}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(
        f'https://kauth.kakao.com/oauth/authorize?client_id={kakao_key}&redirect_uri={redirect_uri}&response_type=code'
    )


def kakao_callback(request):
    try:
        code = request.GET['code']
        data = {
            'grant_type': 'authorization_code',
            'client_id': env('KAKAO_KEY'),
            'redirect_uri': env('REDIRECT_URI'),
            'code': code
        }
        url = "https://kauth.kakao.com/oauth/token"
        res = requests.post(url, data)
        access_token = res.json().get('access_token')
        user_info = requests.get('https://kapi.kakao.com/v2/user/me',
                                 headers={'Authorization': f'Bearer ${access_token}'})
        email = user_info.json()['kakao_account']['email']
        error = res.json().get('error', None)
        if error is not None:
            raise KakaoException('authorization code을 얻을 수 없습니다.')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(email=email)
            user.set_unusable_password()
            user.save()
        messages.success(request, f"환영합니다 {user.email}님")
        login(request, user)
        return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("users:login"))


def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
