from telnetlib import STATUS
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import *
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *
# Create your views here.

def marcket_list(request):

    marckets = Marcket.objects.all()

    serializer = ProductSerializer(marckets, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def marcket_create(request):

    if request.method == 'GET':
        marckets = Marcket.objects.all()
        serializer = MarcketListSerializer(marckets,many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = MarcketListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=STATUS.HTTP_201_CREATED)

@api_view(['GET','DELETE','PATCH'])
@permission_classes([IsAuthorOrReadonly])
def marcket_detail_update_delete(request, marcket_pk):
    marcket = get_object_or_404(Marcket,pk=marcket_pk)

    if request.method=='GET':
        serializer = MarcketSerializer(marcket)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        marcket.delete()
        data={'marcket':marcket_pk}
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = MarcketSerializer(instance=marcket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthorOrReadonly])
def product_create(request,marcket_pk):
    marcket = get_object_or_404(Marcket, pk=marcket_pk)
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products,many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(marcket=marcket)
            return Response(data=serializer.data, status=STATUS.HTTP_201_CREATED)

@api_view(['GET','DELETE','PATCH'])
@permission_classes([IsAuthorOrReadonly])
def product_detail_update_delete(request, marcket_pk,product_pk):
    product = get_object_or_404(Product,pk=product_pk)

    if request.method=='GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        data={'product':product_pk}
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthorOrReadonly])
def option_create(request,marcket_pk,product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'GET':
        options = Option.objects.all()
        serializer = OptionSerializer(options,many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            return Response(data=serializer.data, status=STATUS.HTTP_201_CREATED)

@api_view(['GET','DELETE','PATCH'])
@permission_classes([IsAuthorOrReadonly])
def option_detail_update_delete(request, marcket_pk,product_pk,option_pk):
    option = get_object_or_404(Option,pk=option_pk)

    if request.method=='GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        option.delete()
        data={'option':option_pk}
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = ProductSerializer(instance=option, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)