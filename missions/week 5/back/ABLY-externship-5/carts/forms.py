from django import forms


class AddMerchandiseForm(forms.Form):
    quantity = forms.IntegerField()
    is_updated = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
