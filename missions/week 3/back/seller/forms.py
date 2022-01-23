from django.forms import ModelForm
from shop.models import Product

class ProductUploadForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'category',
                  'image']


# 'market','description', 'price', 'detail',