from django import forms

from .models import *


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address', 'postal_code', 'extra_address', 'phone']
