from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_id', 'user_pw', 'user_email']
        widgets = {
            'user_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '이름'
                }
            ),
            'user_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '아이디'
                }
            ),
            'user_pw': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호'
                }
            ),
            'user_email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '이메일'
                }
            ),
        }
