from django import forms
from django.db.models import fields
from .models import Question, Comment


class QuestionLoadForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'content',
        ]


class QuestionSaveForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'user',
            'merchandise',
            'title',
            'content',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'id',
            'question',
            'merchandise',
            'content',
        ]