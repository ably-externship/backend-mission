from rest_framework import serializers
from .models import Market

# Market 관련
# 리스트
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'