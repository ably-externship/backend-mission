from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름",
        })
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(8자 이상)",
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 확인",
        })
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "placeholder": "이메일",
        })
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
