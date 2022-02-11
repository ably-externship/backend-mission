from django import forms

from .models import *


class BuyerForm(forms.Form):
    buyer_name = forms.CharField(label='이름')
    buyer_email = forms.EmailField(label='이메일')
    buyer_tel = forms.CharField(label='전화 번호', required=True)


class PaymentMethodForm(forms.Form):
    payment_method = forms.ModelChoiceField(label='결제 수단', queryset=PaymentMethod.objects.all(),
                                            widget=forms.RadioSelect)
