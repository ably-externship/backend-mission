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

    # def save(self, *args, **kwargs):
    #     user = super().save(commit=False)
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     user.username = email
    #     user.set_password(password)
    #     user.save()
