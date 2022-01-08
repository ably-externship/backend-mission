from django.forms import ModelForm
from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




# 사용자의 자기 정보 변경 폼
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active')

    def clean_password(self):
        return self.initial["password"]

class MallsquestionForm(ModelForm):
    class Meta:
        model = MallsQuestion
        fields = ['q_num','subject', 'content', 'user', 'date', 'rep', 'reply']


class MallslistForm(ModelForm):
    class Meta:
        model = MallsList
        fields = ['id','shop', 'kind', 'date', 'description', 'url', 'img_url']

class MallsitemForm(ModelForm):
    class Meta:
        model = MallsItems
        fields = ['id', 'num', 'name', 'amount', 'price', 'useyn', 'kind' , 'description', 'image_url', 'url', 'regdate']

class MallshttpForm(ModelForm):
    class Meta:
        model = Mallshttp
        fields = ['name','httpobjects']