from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('market_pk', 'name', 'price', 'sold_out_yn', 'descriptions', 'create_date')