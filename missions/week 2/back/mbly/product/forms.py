from django import forms
from product.models import Question, Answer

class ProductSearchForm(forms.Form):
    search_word = forms.CharField(label = 'Search Word')
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','content'] # QuestionForm에서 사용할 QUestion 모델의 속성

        labels ={
            'subject':'제목',
            'content':'내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

        labels = {
            'content':'내용',
        }
