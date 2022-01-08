import secrets

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import AccountCreateForm, FindusernameForm, ResetpasswordForm
from account.models import User


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
        form = FindusernameForm(request.POST)
        if form.is_valid():
            target_email = form.cleaned_data['email']
            try:
                find_user = User.objects.get(email=target_email)
            except User.DoesNotExist:
                return HttpResponse('입력한 이메일에 해당하는 유저가 없습니다.')

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
                return HttpResponse('입력한 이메일에 해당하는 유저가 없습니다.')

            token = secrets.token_urlsafe()
            
            url = 'http://127.0.0.1:8000/change_password/reset=' + token

            subject = '비밀번호 재설정 이메일 입니다.'
            content = '안녕하세요.' \
                      '비밀번호 변경 URL 입니다.'

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
