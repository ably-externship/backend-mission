from rest_framework import serializers

from market.models import Market


class MarketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'company_name')