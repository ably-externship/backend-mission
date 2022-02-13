from ..models import MarketDailySales, ProductDailySales
from rest_framework import serializers
class ProductDailySalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDailySales
        fields = ('__all__')

class MarketDailySalesSerializer(serializers.ModelSerializer):
    class Meta:
            model = MarketDailySales
            fields = ('__all__')
