from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer
from mutbly.models import Item, Quantity, Question
from rest_framework.permissions import IsAdminUser

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

  