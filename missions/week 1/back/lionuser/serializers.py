from rest_framework import serializers

from .models import Lionuser
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, get_user_model

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
        user = Lionuser.objects.create(username = validated_data['username'], email=validated_data['email'], user_type = validated_data['user_type'], shop = validated_data['shop'], is_staff=True)
        user.set_password(validated_data['password'])#

        user.save()
        return user

class LionuserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = Lionuser
        fields = ['username', 'password']

    # def validate(self, data):
    #     username = data.get("username", None)
    #     password = data.get("password", None)
    #     try:
    #         user = authenticate(username=username, password=password)
    #     except:
    #         return Response({'status': 403, 'errors': "errors", 'message': '유저 로그인 에러입니다.'})
    #
    #     return user

#token에 payload추가 이걸 사용해서 만들지 않으면, 페이로드에 user_id 만 들어가
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token['gender_display'] = user.get_gender_display()
        # token['gender'] = user.get_gender_display()
        token['name'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff #is_staff
        # token['is_active'] = user.is_active
        token['user_type'] = user.user_type
        token['shop'] = user.shop.id

        return token

class ApiRefreshRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass

