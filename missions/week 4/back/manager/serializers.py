from shop.models import Product, Inventory
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# admin만 토큰 발행 ---
class ManagerTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_superuser == True:
            token = super().get_token(user)
            token['email'] = user.email
            token['is_superuser'] = user.is_superuser
            token['is_staff'] = user.is_staff
            return token


# 인벤토리 ---
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'color',
            'size',
            'stock',
            'product'
        ]


# 상품 ---
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    inventories = InventorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'seller',
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