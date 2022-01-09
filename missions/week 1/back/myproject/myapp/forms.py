from django.forms import ModelForm
from .models import *


class BoardForm(ModelForm):
    class Meta:
        model = User
        fields = ['id', 'pw', 'name', 'id_num',
                  'phone', 'email']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['id', 'pw', 'name', 'id_num',
                  'phone', 'email']
