from rest_framework import serializers
from django.contrib.auth.models import User
from market.api.serializers import MarketSerializer

class UserSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only= True)
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','username','email','is_staff','market',)
