from django.forms import ModelForm
from product.models import Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'size', 'count',
                  'description', 'image', 'seller']
