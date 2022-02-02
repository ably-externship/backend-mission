from rest_framework import serializers

from contents.models import Product, Comment, Image, Category, Brand


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


# Image Serializer
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    comment_product = CommentSerializer(many=True, read_only=True)
    image_product = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    product_brand = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'