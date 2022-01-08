from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(label='제품 이름')

