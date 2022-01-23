from rest_framework import serializers 
from markets.models import Product

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product # 모델 설정 
        fields = ('name', 'market', 'price','sale_price', 'is_hidden', 'cate_item')
