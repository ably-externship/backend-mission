from rest_framework import serializers
from .models import Product, Product_option


# Product 관련
# 리스트
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 상세
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 생성
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'sale_price', 'description', 'image', 'image_detail', 'is_hidden', 'is_sold_out', 'reg_date', 'update_date', 'market']

# 수정
class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'sale_price', 'description', 'image', 'image_detail', 'is_hidden', 'is_sold_out', 'update_date', 'market']


# ProductOption 관련