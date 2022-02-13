from ..models import MarketDailySales, ProductDailySales
from rest_framework import serializers
from market.api.serializers import MarketSerializer
from product.api.serializers import ProductSerializer
class ProductDailySalesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    

    class Meta:
        model = ProductDailySales
        fields = ('__all__')

class MarketDailySalesSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only= True)
    class Meta:
            model = MarketDailySales
            fields = ('__all__')
