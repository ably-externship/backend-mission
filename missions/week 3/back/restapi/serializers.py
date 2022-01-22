# serializers.py
from rest_framework import serializers
from accounts.models import User
from base.models import MallsList, MallsItem, Category, MallsQuestion, MallsAnswer

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class MallsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallsList
        fields = ('name', 'description', 'url', 'img_url')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class MallsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallsItem
        fields = ('id', 'num', 'name', 'amount', 'price', 'sale_price', 'is_deleted', 'delete_date',
         'is_hidden', 'is_sold_out', 'category', 'kind', 'description','img_url','url')


class MallsQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallsQuestion
        fields = ('q_num', 'author', 'title', 'text', 'reply', 'created_date', 'published_date')

class MallsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallsAnswer
        fields = ('q_num', 'reg_date', 'update_date', 'answer')
