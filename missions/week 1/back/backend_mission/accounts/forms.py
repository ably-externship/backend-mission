from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


# class SignupForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].required = True
#         self.fields['email'].required = True
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'email']
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if email:
#             qs = User.objects.filter(email=email)
#             if qs.exists():
#                 raise forms.ValidationError("이미 등록된 이메일 주소 입니다.")
#             return email


class AccountCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소 입니다.")
            return email


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']
