from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from account.models import User


class AccountCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 아이디 입니다.")
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소 입니다.")
            return email


class FindusernameForm(Form):
    email = forms.EmailField(label='이메일')


class ResetpasswordForm(Form):
    email = forms.EmailField(label='이메일')


class ChangePasswordForm(Form):
    password1 = forms.CharField(label='변경 비밀번호', widget=forms.PasswordInput())
    password2 = forms.CharField(label='변경 비밀번호 확인', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('패스워드 변경과 확인이 다릅니다.')

        return cleaned_data
