from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .serializer import ProductSerializer 
from markets.models import Product 

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
