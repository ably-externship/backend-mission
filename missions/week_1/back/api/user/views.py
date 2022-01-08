from datetime import datetime, timedelta
import bcrypt
import jwt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..views import BaseView
from .forms import LoginForm
from missions.week_1.back.crud.sql.meta.user import UserCrud
from missions.week_1.back.mbly.settings import JWT_AUTH


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

    @classmethod
    def make_password(cls, password):
        if password and isinstance(password, str):
            bcrypt_password = bcrypt.hashpw(cls.encode_utf_8(password), bcrypt.gensalt())
            return bcrypt_password

        return None


def login_view(request):
    parameter = BaseView.get_parameter(request)

    user = UserCrud.get_user(parameter.get('user_id'))
    if not user:
        data = {'message': '아이디가 없습니다. 회원가입 페이지로 이동합니다'}
        return render(request, 'page/register.html', data)

    login_input_password = parameter.get('password')
    user_password = user[0].get('password')

    if not UserBaseView.check_password(login_input_password, user_password):
        data = {'message': '비밀번호를 확인해주세요'}
        return render(request, 'page/login.html', data)

    payload = {
        'id': parameter.get('user_id'),
        'password': login_input_password,
        'expireTime': JWT_AUTH['JWT_EXPIRATION_DELTA']
    }

    access_token = jwt.encode(
        payload,
        JWT_AUTH['JWT_SECRET_KEY'],
        JWT_AUTH['JWT_ALGORITHM']
    )

    print(access_token)

    data = {'access_token': access_token}
    return render(request, 'page/login.html', data)


def register_view(request):
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
    return render(request, 'page/product_list.html', {})


class LogoutView(UserBaseView):
    pass


