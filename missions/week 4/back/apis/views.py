from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MasterAdminSerializer, BrandAdminSerializer, RegisterBrandSerializer
from mutbly.models import Item, Quantity, Question, Brand
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


class MasterAdminViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = MasterAdminSerializer
  
class BrandAdminViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = BrandAdminSerializer


class RegisterBrandAPIView(APIView):
  queryset = Brand.objects.all()
  serializer_class = RegisterBrandSerializer
  
  def post(self, request) :
    user = request.user
    print(user)
    serializer = RegisterBrandSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid() :
      serializer.save()
      return Response(serializer.data, status=201)
    else :
      return Response(serializer.errors, status=400)
    
    
    