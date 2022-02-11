from django.db import transaction
from rest_framework.serializers import ModelSerializer

from market.models import Market
from market_sns.api.serializers import MarketSnsSerializer, MarketSnsCreateSerializer


class MarketDetailSerializer(ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'company_name')


class MarketListSerializer(ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'company_name', 'user_fk', 'create_date')


class MarketSelectSerializer(ModelSerializer):
    market_sns = MarketSnsSerializer(many=True)
    class Meta:
        model = Market
        fields = ('id', 'company_name', 'user_fk', 'create_date', 'market_sns')


class MarketCreateSerializer(ModelSerializer):
    market_sns = MarketSnsCreateSerializer(many=True, required=False)

    class Meta:
        model = Market
        fields = ('id', 'company_name', 'company_number', 'user_fk', 'market_sns')

    @transaction.atomic
    def create(self, validated_data):
        market_options = validated_data.pop('market_sns', [])
        market = Market.objects.create(**validated_data)

        market_options = list(map(lambda market_sns: {**market_sns, "market_pk": market.id}, market_options))

        for market_option in market_options:
            market_option_serializer = MarketSnsSerializer(data=market_option)

            market_option_serializer.is_valid(raise_exception=True)
            market_option_serializer.save()

        return market

class MarketPatchSerializer(ModelSerializer):

    class Meta:
        model = Market
        fields = ('id', 'company_name', 'company_number', 'user_fk')
