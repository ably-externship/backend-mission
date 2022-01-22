from rest_framework import serializers
from mutbly.models import Item, Quantity, Question




class ItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Item       
        fields = '__all__' 
        
