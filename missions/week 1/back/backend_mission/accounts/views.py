from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from .decorators import account_owner
from .forms import SignupForm, AccountUpdateForm, AccountCreateForm
from .models import User

has_ownership = [login_required, account_owner]


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('base')
    template_name = 'accounts/create.html'


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

    from django.core.mail.message import EmailMessage


# def send_email(request):
#     subject = "message"
#     to = ["min949494@gmail.com"]
#     from_email = "min949494@gmail.com"
#     message = "메지시 테스트"
#     EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
