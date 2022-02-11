from django.forms import models
from ..models import Product, RealProduct
from rest_framework import serializers
from market.api.serializers import MarketSerializer
class RealProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealProduct
        fields = ('reg_date','update_date','option_1_type','option_1_name','option_1_display_name','option_2_type','option_2_name','option_2_display_name','is_sold_out','is_hidden','add_price','stock_quantity')
        read_only_fields = ('reg_date','update_date')

class ProductSerializer(serializers.ModelSerializer):
    realproduct_set = RealProductSerializer(read_only = True,many=True)
    market = MarketSerializer(read_only= True)

    class Meta:
            model = Product
            fields = ('__all__')
            read_only_fields = ('market',)
