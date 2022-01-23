from ..models import Market
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('__all__')

    def validate_name(self, name,site_url):
        if len(Market.objects.filter(name=name))>1 and not site_url: # 중복된 마켓명이고 site_url을 입력하지 않은 경우
            return serializers.ValidationError("site_url을 입력해주세요")
