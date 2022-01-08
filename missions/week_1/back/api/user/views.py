from datetime import datetime
import bcrypt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..views import BaseView
from .forms import LoginForm
from missions.week_1.back.crud.sql.meta.user import UserCrud


class UserBaseView(BaseView):
    @classmethod
    def check_password(cls, input_password, user_password):
        if input_password:
            check = bcrypt.checkpw(
                cls.encode_utf_8(input_password),
                cls.encode_utf_8(user_password)
            )
            return check

        return False

    @classmethod
    def encode_utf_8(cls, value):
        if value and isinstance(value, str):
            return value.encode('utf-8')

        return None


def login_view(request):
    parameter = BaseView.get_parameter(request)

    user = UserCrud.get_user(parameter.get('user_id'))
    if not user:
        data = {'message': '아이디가 없습니다. 회원가입 페이지로 이동합니다'}
        render(request, 'page/register.html', data)

    login_input_password = request.get('password')
    user_password = user[0].get('password')

    return render(request, 'page/login.html', data)


def register_view(request):
    parameter = BaseView.get_parameter(request)

    register = {}
    register['user_id'] = parameter.get('id')
    register['password'] = parameter.get('password')
    register['email'] = parameter.get('email')
    register['name'] = parameter.get('name')
    register['sex'] = int(parameter.get('sex') or 2)
    register['phone'] = parameter.get('phone')
    register['address'] = parameter.get('address')
    register['maritial_status'] = parameter.get('maritial_status')
    now = datetime.now()
    register['created_at'] = now
    register['updated_at'] = now

    try:
        UserCrud.create_user(register)
        return render(request, 'page/product_list.html', {})
    except BaseException as e:
        return render(request, 'page/register.html', {})


class LogoutView(UserBaseView):
    pass


