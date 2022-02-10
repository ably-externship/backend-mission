from rest_framework import serializers
from .models import Cart
from product.serializers import *

# Cart 관련
# 리스트
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    product_option = OptionSerializer(many=True)
    class Meta:
        model = Cart
        # fields = ['user', 'product']
        fields = '__all__'