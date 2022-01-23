from shop.models import Product, Inventory
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# admin만 토큰 발행 ---
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_superuser == True:
            token = super().get_token(user)
            return token


# 인벤토리 ---
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


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
            'market',
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