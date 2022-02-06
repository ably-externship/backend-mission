from rest_framework import serializers
from .models import Seller
from shop.models import Product, Inventory
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# 셀러(is_staff 일 경우) 토큰 발행 ---
class SellerTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_staff == True:
            token = super().get_token(user)
            token['email'] = user.email
            token['is_staff'] = user.is_staff
            return token

# 유저 ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'email',
        ]


# 셀러 ---
class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = [
            'user',
            'market',
            'phone',
            'address'
        ]


# 인벤토리 ---
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'color',
            'size',
            'stock'
        ]

# 상품 ---
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    inventories = InventorySerializer(many=True, read_only=True)
    market_name = serializers.SerializerMethodField(source='get_market_name')
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'seller',
            'market_name',
            'description',
            'price',
            'slug',
            'sale_price',
            'display',
            'detail',
            'image',
            'image_url',
            'inventories'
        ]
    # 마켓명 가져오기
    def get_market_name(self, obj):
        return obj.seller.market