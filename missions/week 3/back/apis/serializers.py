from rest_framework import serializers

from contents.models import Product, Comment


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'product', 'author', 'contents',
        )


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    comment_product = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'