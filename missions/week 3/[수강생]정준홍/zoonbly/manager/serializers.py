from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from main.models import *

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

