from rest_framework import serializers

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'name', 'price', 'sold_out_yn', 'create_date')


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('market_pk', 'category_fk', 'name', 'price', 'descriptions')


class ProductPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'category_fk', 'name', 'price', 'descriptions')
