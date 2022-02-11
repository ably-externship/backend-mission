from rest_framework import serializers
from django.contrib.auth.models import User
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


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    # def get_token(self, obj):
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    #
    #     payload = jwt_payload_handler(obj)
    #     token = jwt_encode_handler(payload)
    #     return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = '__all__'