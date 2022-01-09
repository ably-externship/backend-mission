from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    
    username = forms.CharField(
        required=True,
        min_length=4,
        max_length=20,
        label="아이디:",
        widget=forms.TextInput(attrs={
            "placeholder": "아이디(영문 소문자/숫자, 4~20자)",
        })
    )
    email = forms.EmailField(
        required=False,
        label="이메일:",
        widget=forms.TextInput(attrs={
            "placeholder": "이메일(선택항목)",
        })
    )
    password1 = forms.CharField(
        required=True,
        min_length=8,
        max_length=16,
        label="비밀번호:",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(영문 대소문자/숫자/특수문자, 8~16자)",
        })
    )
    password2 = forms.CharField(
        required=True,
        min_length=8,
        max_length=16,
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 확인",
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        if email == '':
            email = None
            self.cleaned_data['email'] = email
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'email',
        ]