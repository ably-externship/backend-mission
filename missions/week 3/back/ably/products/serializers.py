from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'market', 'name', 'price', 'color', 'size', 'description', 'image', 'created_at']
