from datetime import datetime
from django.shortcuts import render
from ..views import BaseView
from missions.week_1.back.crud.sql.meta.user import UserCrud


class UserBaseView(BaseView):
    pass


def login_view(request):
    return render(request, 'page/login', {})


def register_view(request):
    return render(request, 'page/registration.html', {})


def create_user(request):
    parameter = BaseView.get_parameter(request)

    password = UserBaseView.make_password(parameter.get('password'))
    now = datetime.now()
    register = {
        'user_id': parameter.get('id'),
        'password': password,
        'email': parameter.get('email'),
        'name': parameter.get('name'),
        'sex': int(parameter.get('sex') or 0),
        'phone': parameter.get('phone'),
        'address': parameter.get('address'),
        'maritial_status': parameter.get('maritial_status'),
        'created_at': now,
        'updated_at': now
    }

    UserCrud.create_user(register)

    return render(request, 'page/login.html', {})


class LogoutView(UserBaseView):
    pass


