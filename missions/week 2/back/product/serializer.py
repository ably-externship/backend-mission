from rest_framework import serializers
from .models import Product, ProductDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id',)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id',)
