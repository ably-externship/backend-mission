from .models import MainCategory, SubCategory, BaseMerchandise, Merchandise
from rest_framework import serializers


class MainCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = [
            'id',
            'name',
        ]


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'maincategory',
            'id',
            'name',
        ]
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['maincategory'] = MainCategoryListSerializer(instance.maincategory).data
        return response


class SellerMerchandiseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id',
            'basemerchandise',
            'full_code',
            'color',
            'size',
            'current_stock',
            'safety_stock',
            'on_sale',
            'on_display',
            'created',
            'updated',
        ]


class SellerMerchandiseNestedListSerializer(serializers.ModelSerializer):
    merchandise = SellerMerchandiseListSerializer(many=True, read_only=True)
    
    class Meta:
        model = BaseMerchandise
        fields = [
            'subcategory',
            'id',
            'seller',
            'common_code',
            'name',
            'standard_price',
            'discounted_price',
            'main_img',
            'sub_img_0',
            'sub_img_1',
            'sub_img_2',
            'created',
            'updated',
            'merchandise',
        ]
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subcategory'] = SubCategoryListSerializer(instance.subcategory).data
        return response


class SellerBaseMerchandiseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMerchandise
        fields = [
            'subcategory',
            'seller',
            'common_code',
            'name',
            'standard_price',
            'discounted_price',
            'main_img',
            'sub_img_0',
            'sub_img_1',
            'sub_img_2',
            'description',
        ]


class SellerMerchandiseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'basemerchandise',
            'full_code',
            'color',
            'size',
            'current_stock',
            'safety_stock',
            'soldout_state',
            'on_sale',
            'on_display',
        ]


class SellerBaseMerchandiseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMerchandise
        fields = [
            'subcategory',
            'name',
            'standard_price',
            'discounted_price',
            'main_img',
            'sub_img_0',
            'sub_img_1',
            'sub_img_2',
            'description',
        ]


class SellerMerchandiseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'color',
            'size',
            'current_stock',
            'safety_stock',
            'soldout_state',
            'on_sale',
            'on_display',
        ]