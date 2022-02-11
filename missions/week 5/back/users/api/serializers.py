from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from product.models import Product


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserAuthResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_hash = serializers.CharField()


class UserAuthResponse:
    def __init__(self, access_token, refresh_hash):
        self.access_token = access_token
        self.refresh_hash = refresh_hash

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "refresh_hash": self.refresh_hash,
        }

# TODO 3주차 설명, 이걸 사용해서 만들지 않으면, 페이로드에 user_id 만 들어갑니다. ㅜㅜ. 특히 is_staff 는 꼭 넣어주세요.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_active'] = user.is_active
        token['market_yn'] = user.market_yn
        # if user.market_yn:
        #     #token['market_id'] = user.market_id.id
        return token