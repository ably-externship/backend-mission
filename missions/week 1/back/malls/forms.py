from django.forms import ModelForm
from .models import *

class MallsForm(ModelForm):
    class Meta:
        model = Malls
        fields = ['title', 'content', 'writer']