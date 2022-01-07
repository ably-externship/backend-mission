from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from base import settings
from .decorators import account_owner
from .forms import AccountUpdateForm, AccountCreateForm
from .models import User

has_ownership = [login_required, account_owner]


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('base')
    template_name = 'accounts/signup.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/update.html'


@method_decorator(has_ownership, 'get')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/delete.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'accounts/password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력






