from telnetlib import STATUS
from django.http import response
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from main.models import *
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

# Create your views here.

def product_list(request):

    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def product_list_create(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)

        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=STATUS.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def product_detail_update_delete(request, product_pk):
    product = get_object_or_404(Product,pk=product_pk)

    if request.method=='GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        data={'product':product_pk}
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)