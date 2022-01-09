from django.shortcuts import render, redirect
from ..views import BaseView
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('api/v1/user/login')


class UserBaseView(BaseView):
    pass


class LoginView(FormView):
    template_name = 'page/login.html'
    form_class = LoginForm
    success_url = 'http://localhost:8000/api/v1/product/list'

    def form_valid(self, form):
        self.request.session['user'] = form.id

        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'page/registration.html'
    form_class = RegisterForm
    success_url = 'login'

