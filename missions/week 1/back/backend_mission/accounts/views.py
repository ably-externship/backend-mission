from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from .decorators import account_owner
from .forms import SignupForm, AccountUpdateForm, AccountCreateForm
from .models import User

has_ownership = [login_required, account_owner ]

def home(request):
    return render(request, 'accounts/home.html')


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('accounts:home')
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
