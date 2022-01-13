from django.forms import ModelForm
from product.models import Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'count',
            'description',
            'image',
            'seller',
        ]
