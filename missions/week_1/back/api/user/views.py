from django.shortcuts import render, redirect
from ..views import BaseView
from .forms import LoginForm
from django.contrib.auth import authenticate, login


class UserBaseView(BaseView):
    pass


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ''
    if not form:
        data = {
            'msg': msg,
        }
        return BaseView.response(request, 'login.html', data)

    if request.method == 'POST':
        if form.is_valid():
            id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            user = authenticate(username=id, password=password)
            if user is not None:
                login(request, user)
                return redirect('api/v1/user/register')
        else:
            msg = 'Error validating the form'

    data = {
        'form': form,
        'msg': msg
    }
    return render(request, 'login.html', data)


def register_view(request):
    _db = 'meta'
    _table = 'customer'
    pass


class LoginView(UserBaseView):
    pass


class LogoutView(UserBaseView):
    pass


