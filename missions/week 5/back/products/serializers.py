from rest_framework import serializers

from markets.serializers import MarketSerializer
from products.models import Product, Category, ProductOption, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'color', 'size', 'stock', 'add_price', 'is_sold_out']


class ProductSerializer(serializers.ModelSerializer):
    market = serializers.CharField(source='market.name')
    category = serializers.CharField(source='category.name', required=False)

    class Meta:
        model = Product
        fields = ['id', 'market', 'category', 'name', 'price', 'is_sold_out', 'is_hidden', 'is_delete']


class ProductDetailSerializer(serializers.ModelSerializer):
    """상품 + 옵션까지"""
    options = ProductOptionSerializer(many=True)
    market = serializers.CharField(source='market.name')
    category = serializers.CharField(source='category.name', required=False)

    class Meta:
        model = Product
        fields = ['id', 'market', 'category', 'name', 'price', 'is_sold_out', 'is_hidden', 'is_delete', 'options']
