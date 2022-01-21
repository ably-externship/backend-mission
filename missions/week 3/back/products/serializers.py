from rest_framework import serializers

from markets.serializers import MarketSerializer
from products.models import Product, Category, ProductOption


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'color', 'size', 'stock', 'add_price', 'is_sold_out']


class ProductSerializer(serializers.ModelSerializer):
    # market = MarketSerializer()       # 여러 정보가 있을 경우 nested 로 처리
    # category = CategorySerializer()
    market = serializers.CharField(source='market.name')
    category = serializers.CharField(source='category.name', required=False)

    class Meta:
        model = Product
        fields = ['id', 'market', 'category', 'name', 'price', 'is_sold_out', 'is_hidden', 'is_delete']
