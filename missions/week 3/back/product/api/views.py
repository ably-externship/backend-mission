from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from common.BaseResponse import BaseResponse
from rest_framework.response import Response
from rest_framework import status

from product.api.serializers import ProductListSerializer, ProductPostSerializer, ProductPutSerializer
from product.models import Product
from rest_framework import exceptions
from common.exception.ErrorMessage import ErrorMessage


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        response = BaseResponse(data=serializer.data, message="AAA", code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if request.method == 'POST':
        product = ProductPostSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(data=product.data, status=status.HTTP_201_CREATED)
        else:
            if product.errors.get('market_pk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.MARKET_NOT_FOUND.code, "message":ErrorMessage.MARKET_NOT_FOUND.message})
            if product.errors.get('category_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code, "message":ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_VALIDATION_ERROR.code, "message":ErrorMessage.PRODUCT_VALIDATION_ERROR.message})


@api_view(['PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def product(request, id):
    if  request.method == 'PUT':
        try:
            Product.objects.select_related('market_pk').get(id=id)
            product = ProductPutSerializer(data=request.data)
            if product.is_valid():
                product.save()
                return Response(data=product.data, status=status.HTTP_201_CREATED)
            else:
                if product.errors.get('market_pk') is not None:
                    raise exceptions.NotFound(
                        detail={'code': ErrorMessage.MARKET_NOT_FOUND.code, "message": ErrorMessage.MARKET_NOT_FOUND.message})
                if product.errors.get('category_fk') is not None:
                    raise exceptions.NotFound(detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code,
                                                      "message": ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
                else:
                    raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_VALIDATION_ERROR.code,
                                                             "message": ErrorMessage.PRODUCT_VALIDATION_ERROR.message})
        except Product.DoesNotExist:
            raise exceptions.NotFound(
                detail={'code': ErrorMessage.PRODUCT_NOT_FOUND.code, "message": ErrorMessage.PRODUCT_NOT_FOUND.message})
    if request.method == 'DELETE':
        try:
            Product.objects.select_related('market_pk').get(id=id)
            product = ProductPutSerializer(data=request.data)
            return Response(data=None, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            raise exceptions.NotFound(
                detail={'code': ErrorMessage.PRODUCT_NOT_FOUND.code, "message": ErrorMessage.PRODUCT_NOT_FOUND.message})

