from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from product.models import Product, ProductOption, CartItem, OrderItem


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
        fields = ['id', 'name', 'author_id', 'seller', 'price', 'image', 'description', 'productoption', ]


class CartItemSerializer(ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    productoption_size = serializers.ReadOnlyField(source='productoption.size')
    productoption_color = serializers.ReadOnlyField(source='productoption.color')

    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'product_id', 'user_id', 'productoption_id', 'product_name', 'productoption_size', 'productoption_color',]


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'user_id', 'product_id', 'productoption_id']
