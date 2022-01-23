from rest_framework import serializers
from product.models import Product, ProductDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # exclude = ('id',)
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ('id',)
