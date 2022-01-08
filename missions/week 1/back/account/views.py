from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from account.decorators import account_owner
from account.forms import AccountUpdateForm, AccountCreateForm, FindusernameForm
from account.models import User

has_ownership = [login_required, account_owner]


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('base')
    template_name = 'account/signup.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'account/update.html'


@method_decorator(has_ownership, 'get')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')
    template_name = 'account/delete.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('account:password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'account/password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력


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
            content = '안녕하세요.'\
                      '아이디 찾기 결과 입니다.'\
                      f'아이디는 {find_user.username} 입니다.'\
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
