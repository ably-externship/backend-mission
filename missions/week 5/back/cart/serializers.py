from rest_framework import serializers
from .models import Cart
from product.serializers import *

# Cart 관련
# 리스트
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_option = OptionSerializer(read_only=True)
    class Meta:
        model = Cart
        # fields = ['user', 'product']
        fields = '__all__'

# 생성
class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        # fields = ['user', 'product']
        fields = '__all__'