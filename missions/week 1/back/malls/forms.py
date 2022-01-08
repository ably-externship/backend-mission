from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password']


class MallsquestionForm(ModelForm):
    class Meta:
        model = MallsQuestion
        fields = ['q_num','subject', 'content', 'user', 'date', 'rep', 'reply']


class MallslistForm(ModelForm):
    class Meta:
        model = MallsList
        fields = ['shop', 'kind', 'date', 'description', 'url', 'img_url']