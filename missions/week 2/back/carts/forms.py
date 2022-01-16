from django import forms

from carts.models import Cart


class CartUpdateForm(forms.ModelForm):
    product = forms.CharField(max_length=14, disabled=True)

    class Meta:
        model = Cart
        fields = ['product', 'product_option', 'quantity']
