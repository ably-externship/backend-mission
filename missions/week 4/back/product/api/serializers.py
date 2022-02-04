from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from product.models import Product, ProductOption


class ProductOptionSerializer(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = [
            'id',
            'size',
            'color',
            'stock_count',
            'product_id',
        ]



class ProductSerializer(ModelSerializer):
    productoption = ProductOptionSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = ['id', 'author_id', 'seller', 'price', 'image', 'description', 'productoption', ]
