from django.views.decorators.csrf import csrf_exempt
from rest_framework import exceptions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.BaseResponse import BaseResponse
from common.exception.ErrorMessage import ErrorMessage
from product.api.serializers import ProductListSerializer, ProductPostSerializer, ProductPutSerializer
from product.models import Product


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def products(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        serializer = ProductListSerializer(product_list, many=True)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if request.method == 'POST':
        product = ProductPostSerializer(data=request.data)
        if product.is_valid():
            product.save()
            response = BaseResponse(data=product.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            if product.errors.get('market_pk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.MARKET_NOT_FOUND.code,
                                                  "message": ErrorMessage.MARKET_NOT_FOUND.message})
            if product.errors.get('category_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code,
                                                  "message": ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_VALIDATION_ERROR.code,
                                                         "message": ErrorMessage.PRODUCT_VALIDATION_ERROR.message})


@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes((IsAuthenticated,))
def product(request, product_id):
    if request.method == 'GET':
        product_model = product_select(product_id)
        serializer = ProductPutSerializer(product_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if request.method == 'PUT':
        product_model = product_select(product_id)
        serializer = ProductPutSerializer(product_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            if serializer.errors.get('market_pk') is not None:
                raise exceptions.NotFound(
                    detail={'code': ErrorMessage.MARKET_NOT_FOUND.code,
                            "message": ErrorMessage.MARKET_NOT_FOUND.message})
            if serializer.errors.get('category_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code,
                                                  "message": ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_VALIDATION_ERROR.code,
                                                         "message": ErrorMessage.PRODUCT_VALIDATION_ERROR.message})
    if request.method == 'DELETE':
        product_model = product_select(product_id)
        product_model.product_status = 'DEACTIVE'
        product_model.save()
        serializer = ProductPutSerializer(product_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)


def product_select(product_id):
    try:
        product_model = Product.objects.select_related('market_pk').get(id=product_id)
        return product_model
    except Product.DoesNotExist:
        raise exceptions.NotFound(
            detail={'code': ErrorMessage.PRODUCT_NOT_FOUND.code, "message": ErrorMessage.PRODUCT_NOT_FOUND.message})
