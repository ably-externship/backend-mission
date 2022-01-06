from django.contrib.auth import get_user_model #, authenticate
from rest_framework import serializers
from rest_framework.compat import SHORT_SEPARATORS
from .models import Lionuser, LionuserManager
from django.contrib.auth.models import update_last_login

from rest_framework_jwt.settings import api_settings

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
Luser = get_user_model()
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    def create(self, validated_data):
        user = Luser.objects.create( # User 생성
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

def authenticate(username=None, password=None):

    UserModel = get_user_model()
    try:

        user = UserModel.objects.get(email=username)

    except UserModel.DoesNotExist:
        return None
    else:
        if user.password == password: #make_password
            return user
    return None

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)

    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        luser = authenticate(username=email, password=password)

        if luser is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(luser)
            jwt_token = JWT_ENCODE_HANDLER(payload) # 토큰 발행
            update_last_login(None, luser)

        except Luser.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': email,
            'token': jwt_token
        }