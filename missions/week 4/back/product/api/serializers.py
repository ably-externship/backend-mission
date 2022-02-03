from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from product.models import Product, ProductOption


# class ProductSerializer(ModelSerializer):
#     class Meta:
#         model = Product
#         fields = [
#             'id',
#             'author',
#             'name',
#             'seller',
#             'price',
#             'image',
#             'description',
#         ]

class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = [
            'id',
            'size',
            'color',
            'stock_count',
        ]


class ProductSerializer(ModelSerializer):

    productoption = ProductOptionSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = ['id', 'author_id', 'seller', 'price', 'image', 'description', 'productoption']


