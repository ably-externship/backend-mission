from rest_framework import serializers
from .models import Product, ProductOptionGroup, ProductOptionGroupItem, ProductImg

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = "__all__"
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['product'] = ProductSerializer(instance.product).data
    #     return response

class ProductSerializer(serializers.ModelSerializer):
    imgs = ProductImgSerializer(many=True, read_only=True, source='productImgs')
    class Meta:
        model = Product
        fields = "__all__" #'__all__' #('id','product_name', 'description',"price","stock","register_date","status","optionGroups","productImgs")

class ProductOptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroup
        fields = ('product','optionGroup','optionItems')

class ProductOptionGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroupItem
        fields = '__all__'


