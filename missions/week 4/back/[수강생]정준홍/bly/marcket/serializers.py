from rest_framework import serializers
from .models import *

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ('product','color','size','price','stock','user')
        # read_only_fields = ('product')

class ProductDetailSerializer(serializers.ModelSerializer):

    option_set = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','name','user','marcket','description','option_set')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','name','user','marcket','description')
        

class MarcketListSerializer(serializers.ModelSerializer):

    product_set = ProductSerializer(many=True, read_only=True)
    product_count = serializers.IntegerField(source='product_set.count',read_only=True)
    class Meta:
        model = Marcket
        fields = ('id','name','user','product_set','product_count')

class MarcketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcket
        fields = ('id','name','user')