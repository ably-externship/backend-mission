from bootstrap5 import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

RADIO_CHOICES = (("GOODS", "상품"), ("PAY", "결재"), ("REFUND", "환불"))


class BoardCreateForm(forms.Form):
    type = forms.ChoiceField(choices=RADIO_CHOICES, label="질문 유형", required=True)
    title = forms.CharField(required=True, max_length=100, label="제목")
    content = forms.CharField(widget=forms.Textarea, label="컨텐츠")

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
