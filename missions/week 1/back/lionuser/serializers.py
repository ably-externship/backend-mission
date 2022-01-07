from rest_framework import serializers

from .models import Lionuser
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(username=username, password=password)
        return user


class LionuserSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(max_length=64)
    # username = serializers.CharField(max_length=128)
    # password = serializers.CharField(max_length=255)
    class Meta:
        model = Lionuser
        fields = '__all__'
    def create(self, validated_data):
        user = Lionuser.objects.create(username = validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LionuserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = Lionuser
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(username=username, password=password)
        return user