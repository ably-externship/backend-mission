from rest_framework import serializers 
from markets.models import Product

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product # 모델 설정 
        fields = ('reg_date','update_date','is_deleted','delete_date',
                'market', 'name', 'display_name', 'price', 'sale_price',
                'is_hidden', 'is_sold_out', 'cate_item', 'hit_count', 'review_count', 'review_point')

