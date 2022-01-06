from rest_framework import serializers
from .models import Product, ProductOptionGroup, ProductOptionGroupItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductOptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroup
        fields = '__all__'

class ProductOptionGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroupItem
        fields = '__all__'
