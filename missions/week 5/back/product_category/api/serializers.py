from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product_category.models import ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'category_status')
