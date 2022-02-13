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
    product_option = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'author_id',
            'seller',
            'price',
            'image',
            'description',
            'product_option',
        ]


class CartItemSerializer(ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_option_size = serializers.ReadOnlyField(source='product_option.size')
    product_option_color = serializers.ReadOnlyField(source='product_option.color')

    class Meta:
        model = CartItem
        fields = [
            'quantity',
            'product_id',
            'user_id',
            'product_option_id',
            'product_name',
            'product_option_size',
            'product_option_color',
        ]


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'quantity',
            'user_id',
            'product_id',
            'product_option_id'
        ]


class BatchOrderSerializer(serializers.Serializer):
    orders = OrderItemSerializer(many=True)
