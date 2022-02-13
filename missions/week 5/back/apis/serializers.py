from rest_framework import serializers
from mutbly.models import Item, Quantity, Question, Brand




class MasterAdminSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Item       
        fields = '__all__' 
        

class BrandAdminSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Item       
        fields = '__all__' 

class RegisterBrandSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Brand     
        fields = '__all__' 