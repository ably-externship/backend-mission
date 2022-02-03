from rest_framework import serializers

from market.api.serializers import MarketDetailSerializer
from product.models import Product
from product_category.api.serializers import ProductCategorySerializer


class ProductListSerializer(serializers.ModelSerializer):
    market_pk = MarketDetailSerializer(read_only=True)
    category_fk = ProductCategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'name', 'price', 'sold_out_yn', 'create_date', 'product_status', 'category_fk')


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('market_pk', 'category_fk', 'name', 'price', 'descriptions')


class ProductPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'category_fk', 'name', 'price', 'descriptions', 'product_status')
