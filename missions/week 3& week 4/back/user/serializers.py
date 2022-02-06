from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_staff']=user.is_staff
        token['is_superuser']=user.is_superuser
        token['username'] = user.username
        token['id'] = user.id

        return token

class ApiRefreshRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'