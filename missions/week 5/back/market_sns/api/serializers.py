from django.db import transaction
from rest_framework import serializers

from market.models import Market
from market_sns.models import MarketSns


class MarketSnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketSns
        fields = ('id', 'market_pk', 'url', 'market_sns')


