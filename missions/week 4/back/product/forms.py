from django import forms
from django.forms import ModelForm
from product.models import Product, ProductOption


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'image',
            'seller',
        ]


class ProductPurchaseForm(forms.Form):
    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)

        options = ProductOption.objects.filter(product=product).order_by('size', 'color')
        choices = []
        for option in options:
            choices.append((option.id, f'{option.size}/{option.color}'))
        if not choices:
            choices = [(0, '재고없음')]

        self.fields['product_option'] = forms.ChoiceField(choices=choices)
        self.fields['product_option'].label = ''
