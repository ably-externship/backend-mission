from rest_framework import serializers

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