from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_recommand
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['username'] = user.username
        token['gender'] = user.get_gender_display()
        token['name'] = user.name
        token['email'] = user.email
        token['is_staff']=user.is_staff
        token['is_active'] = user.is_active
        token['is_superuser']=user.is_superuser



        return token

class ApiRefreshRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_recommand
        fields = '__all__'
