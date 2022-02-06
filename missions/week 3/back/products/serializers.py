from rest_framework import serializers

from .models import Product
from vendors.models import Vendor
from users.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description',
                  'price', 'image', 'quantity', 'reg_date', 'vendor']


class VendorSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'products']
