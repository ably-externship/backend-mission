from django.db.models import fields
from rest_framework import serializers
from .models import *
from accounts.models import AuthUser



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.CharField(source='model_method')
    class Meta:
        model = Item
        fields = ['id_item','color','size','name','price','stock','store_id_store','url']


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ['id_store', 'name', 'detail']
