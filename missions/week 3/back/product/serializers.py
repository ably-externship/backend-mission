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

# 해당 제품 찾기
class ProductFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']



# ProductOption 관련
# 리스트
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_option
        fields = '__all__'

# 생성
class OptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_option
        fields = ['id', 'reg_date', 'update_date', 'opt1_type', 'opt1_name', 'opt1_price', 'opt1_stock', 'product']

