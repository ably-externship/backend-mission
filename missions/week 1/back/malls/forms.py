from django.forms import ModelForm
from .models import *

class MallsquestionForm(ModelForm):
    class Meta:
        model = MallsQuestion
        fields = ['q_num','subject', 'content', 'user', 'date', 'rep', 'reply']
