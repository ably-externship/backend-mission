from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
