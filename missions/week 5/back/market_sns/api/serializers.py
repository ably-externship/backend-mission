from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from market.models import Market
from market_sns.models import MarketSns


class MarketSnsSerializer(ModelSerializer):
    class Meta:
        model = MarketSns
        fields = ('id', 'market_pk', 'url')


class MarketSnsCreateSerializer(ModelSerializer):
    class Meta:
        model = MarketSns
        fields = ('id', 'market_pk', 'url')
        extra_kwargs = {
            'market_pk': {'required': False, 'allow_null': True},
        }

        # 이거 쓰면 입력시 product 를 필요로 함, 그런데 등록시에는 product를 알 수 없음..
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=model.objects.all(),
        #         fields=('product', 'option_1_name', 'option_2_name'),
        #         message="product and option_1_name and option_2_name should be unique together"
        #     )
        # ]
