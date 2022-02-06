from rest_framework import serializers
from product.models import Product, ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ('id', 'product_id')

    # def create(self, validated_data):
    #     print(validated_data)
    #     print(self)
    #     product_detail = ProductDetail.objects.create(**validated_data)
    #     return product_detail


class ProductSerializer(serializers.ModelSerializer):
    options = ProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        # exclude = ('id',)
        # fields = '__all__'
        fields = ('product_code', 'product_name', 'product_price', 'main_image', 'detail_image', 'category', 'options')

    # def create(self, validated_data):
    #     options_data = validated_data.pop('options')
    #     images = self.context['request'].FILES
    #     # main_image = validated_data.pop('main_image')
    #     # detail_image = validated_data.pop('detail_image')
    #     print(images)
    #     product = Product.objects.create(**validated_data)
    #     for option in options_data:
    #         ProductDetail.objects.create(options=product, **option)
    #     return product

