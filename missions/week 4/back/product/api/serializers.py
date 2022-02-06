from django.db import transaction
from rest_framework import serializers

from market.api.serializers import MarketDetailSerializer
from product.models import Product
from product_category.api.serializers import ProductCategorySerializer
from product_option.api.serializers import ProductOptionCreateSerializer


class ProductListSerializer(serializers.ModelSerializer):
    market_pk = MarketDetailSerializer(read_only=True)
    category_fk = ProductCategorySerializer(read_only=True)
    product_option = ProductOptionCreateSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'name', 'price', 'sold_out_yn', 'create_date', 'update_date', 'product_status', 'category_fk', 'product_option')


class ProductPostSerializer(serializers.ModelSerializer):
    product_options = ProductOptionCreateSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'category_fk', 'name', 'price', 'descriptions', 'product_options')

    @transaction.atomic
    def create(self, validated_data):
        product_options = validated_data.pop('product_options', [])
        product = Product.objects.create(**validated_data)

        product_options = list(map(lambda product_option: {**product_option, "product_pk": product.id}, product_options))

        for product_option in product_options:
            product_option_serializer = ProductOptionCreateSerializer(data=product_option)

            product_option_serializer.is_valid(raise_exception=True)
            product_option_serializer.save()

        return product


class ProductPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'market_pk', 'category_fk', 'name', 'price', 'descriptions', 'product_status')
