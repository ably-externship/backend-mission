import datetime
import jwt
from django import forms
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from missions.week_1.back.crud.sql.meta.user import UserCrud
from missions.week_1.back.mbly.settings import JWT_AUTH


class RegisterForm(forms.Form):
    user_id = forms.CharField(
        error_messages={
            'required': 'id를 입력해주세요'
        },
        max_length=64,
        label='아이디',
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )
    name = forms.CharField(
        error_messages={
            'required': '본인의 이름을 입력해주세요'
        },
        max_length=64,
        label='이름',
    )
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64,
        label='이메일',
    )
    phone = forms.IntegerField(
        error_messages={
            'required': '본인의 핸드폰 번호를 입력해주세요'
        },
        label='핸드폰 번호',
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        name = cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                user = User(
                    id=user_id,
                    user_id=user_id,
                    email=email,
                    name=name,
                    phone=phone,
                    password=make_password(password),
                )
                user.created_dt = datetime.datetime.now()
                user.update_at = datetime.datetime.now()
                self.insert_user(user)

    def insert_user(self, user):
        now = datetime.datetime.now()
        form = {
            'user_id': user.user_id,
            'password': user.password,
            'email': user.email,
            'name': user.name,
            'phone': user.phone,
            'created_at': now,
            'updated_at': now
        }

        UserCrud.create_user(form)


class LoginForm(forms.Form):
    id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=64,
        label='아이디',
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')

        if id and password:
            try:
                user = UserCrud.get_user(id)
            except BaseException as e:
                self.add_error('id', f'입력하신 유저가 없습니다. {e.args}')
                return
            if not check_password(password, user[0].get('password')):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.id = user[0].get('id')
                payload = {
                    'id': id,
                    'password': password,
                    'expireTime': JWT_AUTH['JWT_EXPIRATION_DELTA']
                }

                access_token = jwt.encode(
                    payload,
                    JWT_AUTH['JWT_SECRET_KEY'],
                    JWT_AUTH['JWT_ALGORITHM']
                )

                print(access_token)
                return redirect('http://localhost:8000/api/v1/product/list')
