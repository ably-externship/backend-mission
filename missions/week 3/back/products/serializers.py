from datetime import datetime

from django.db import transaction
from rest_framework.serializers import ModelSerializer

from products.models import ProductList, Product, ProductHistory, ProductOption, ProductImage

class ProductListSerializer(ModelSerializer):

    class Meta:
        model = ProductList
        fields = '__all__'

class ProductHistorySerializer(ModelSerializer):

    class Meta:
        model = ProductHistory
        fields = ['name', 'price', 'discount_price']

class ProductOptionSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = ['color', 'size', 'stock']

class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['image_url']

class ProductSerializer(ModelSerializer):
    producthistory_set = ProductHistorySerializer(many=True)
    productoption_set = ProductOptionSerializer(many=True)
    productimage_set = ProductImageSerializer(many=True)

    def create(self, validated_data):

        options = validated_data.pop('productoption_set')
        images = validated_data.pop('productimage_set')
        histories = validated_data.pop('producthistory_set')

        with transaction.atomic():
            product = Product.objects.create(**validated_data)
            now = datetime.now()
            for history in histories:
                ProductHistory.objects.create(product=product, created_at = now, **history)
            for option in options:
                ProductOption.objects.create(product=product, **option)
            for image in images:
                ProductImage.objects.create(product=product, **image)

            return product

    class Meta:
        model = Product
        fields = ['seller', 'product_subcategory', 'main_image_url', 'producthistory_set', 'productoption_set', 'productimage_set']

class ProductHistoryUpdateSerializer(ModelSerializer):

    class Meta:
        model = ProductHistory
        fields = ['name', 'price', 'discount_price', 'is_sold_out', 'is_displayed', 'updated_at', 'is_deleted']