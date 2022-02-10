from rest_framework import serializers
from .models import Product, Product_option, Product_qna
from market.serializers import MarketSerializer

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



# Product 관련
# 리스트
class ProductSerializer(serializers.ModelSerializer):
    product_options = OptionSerializer(many=True)
    market = MarketSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'sale_price', 'description',
                  'image', 'image_detail', 'is_hidden', 'is_sold_out', 'reg_date',
                  'hit_count', 'like_count', 'update_date', 'market', 'product_options']

# 상세
class ProductDetailSerializer(serializers.ModelSerializer):
    product_options = OptionSerializer(many=True)
    market = MarketSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'sale_price', 'description',
                  'image', 'image_detail', 'is_hidden', 'is_sold_out', 'reg_date',
                  'hit_count', 'like_count', 'update_date', 'market', 'product_options']

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



# ProductQna 관련
# 리스트
class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_qna
        fields = '__all__'


# 생성
class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_qna
        fields = '__all__'