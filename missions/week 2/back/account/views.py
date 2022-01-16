import secrets

import requests
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import AccountCreateForm, FindusernameForm, ResetpasswordForm, ChangePasswordForm
from account.models import User
from django.shortcuts import redirect


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('base')
    template_name = 'account/signup.html'


def find_username_view(request):
    if request.method == 'GET':
        return render(
            request,
            'account/find_username.html',
            context={
                'form': FindusernameForm(),
            }
        )

    elif request.method == 'POST':
        # email 로 아이디 찾기
        form = FindusernameForm(request.POST)
        if form.is_valid():
            target_email = form.cleaned_data['email']
            try:
                find_user = User.objects.get(email=target_email)
            except User.DoesNotExist:
                messages.info(request, '입력한 이메일에 해당하는 유저가 없습니다.')
                return redirect(request.META['HTTP_REFERER'])

            # 이메일 발송
            subject = '멋블리 아이디 찾기 결과 안내'
            content = '안녕하세요.' \
                      '아이디 찾기 결과 입니다.' \
                      f'아이디는 {find_user.username} 입니다.' \
                      '감사합니다.'

            send_mail(
                subject,
                content,
                'min949494@gmail.com',
                [
                    target_email,
                ],
                fail_silently=True,
            )
            return render(
                request,
                'account/find_username_form_result.html',
                context={
                    'target_email': target_email,
                }
            )


def reset_password_view(request):
    if request.method == 'GET':
        return render(request,
                      'account/reset_password.html',
                      context={
                          'form': ResetpasswordForm(),
                      }
                      )
    elif request.method == 'POST':
        form = ResetpasswordForm(request.POST)
        if form.is_valid():
            target_email = form.cleaned_data['email']
            try:
                find_user = User.objects.get(email=target_email)
            except User.DoesNotExist:
                messages.info(request, '입력한 이메일에 해당하는 유저가 없습니다.')
                return redirect(request.META['HTTP_REFERER'])

            token = secrets.token_urlsafe()
            find_user.tmp_token = token
            find_user.save()
            # 1회성 패스워드 리셋 URL
            url = f'http://127.0.0.1:8000/accounts/change_password/?reset_token={token}'

            subject = '비밀번호 재설정 이메일 입니다.'
            content = '안녕하세요.' \
                      '비밀번호 변경 URL 입니다.' \
                      f'URL : {url}'

            send_mail(
                subject,
                content,
                'min949494@gmail.com',
                [
                    target_email,
                ],
                fail_silently=True,
            )
    return render(
        request,
        'account/reset_password_form_result.html',
        context={
            'target_email': target_email,
        }
    )


def change_password_view(request):
    if request.method == 'GET':
        token = request.GET.get('reset_token')

        try:
            user = User.objects.get(tmp_token=token)
        except User.DoesNotExist:
            return HttpResponse('잘못된 접근입니다.')

        return render(
            request,
            'account/change_password_form.html',
            context={
                'token': token,
                'user': user,
                'form': ChangePasswordForm()
            }
        )
    elif request.method == 'POST':
        token = request.POST.get('token')

        try:
            user = User.objects.get(tmp_token=token)
        except User.DoesNotExist:
            return HttpResponse('잘못된 접근입니다.')

        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password1'])
        else:
            messages.info(request, '비밀번호 변경, 확인이 서로 다릅니다.')
            return redirect(request.META['HTTP_REFERER'])
        user.tmp_token = None
        user.save()

        return redirect('product:list')


def oauth(request):
    code = request.GET['code']
    print('code = ' + str(code))

    client_id = 'a37a43d7902878faaba209dbe6cee083'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    access_token_request_uri = 'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&'

    access_token_request_uri += 'client_id=' + client_id
    access_token_request_uri += '&redirect_uri=' + redirect_uri
    access_token_request_uri += '&code=' + code

    print(access_token_request_uri)

    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()
    access_token = json_data['access_token']

    print('access_token = ' + str(access_token))

    user_profile_info_uri = 'https://kapi.kakao.com/v2/user/me?access_token='
    user_profile_info_uri += str(access_token)
    print(user_profile_info_uri)

    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    user_email = user_json_data['kakao_account']['email']
    user_nickname = user_json_data['kakao_account']['profile']['nickname']
    print(user_nickname)
    print(user_email)

    try:
        user = User.objects.get(email=user_email)

    except User.DoesNotExist:
        user = User.objects.create_user(username=user_nickname, email=user_email)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('base')


def kakao_login_view(request):
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    client_id = 'a37a43d7902878faaba209dbe6cee083'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'


    return redirect(login_request_uri)
