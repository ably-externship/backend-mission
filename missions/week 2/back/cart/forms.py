from django import forms


class AddProductForm(forms.Form):
    quantity = forms.IntegerField(label="수량을 입력하세요")
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # opt_size = forms.CharField()
    # opt_price = forms.IntegerField()