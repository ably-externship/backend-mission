from django.forms import ModelForm
from .models import *


class BoardForm(ModelForm):
    class Meta:
        model = User
        fields = ["id", "username", "password1", "password2", "email"]
