from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id_item','color','size','name','price','stock','store_id_store']