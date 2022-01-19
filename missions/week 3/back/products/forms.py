from django import forms
from .models import Question


class SearchForm(forms.Form):
    name = forms.CharField(label='제품 이름')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content']
        labels = {
            "content": "질문내용"
        }
