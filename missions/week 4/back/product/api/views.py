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
    # 사용자가  Market 인지 체크
    market_yn = request.auth.payload['market_yn']

    if request.method == 'GET':
        if market_yn:
            market_id = request.auth.payload['market_id']
            product_list = Product.objects\
                .prefetch_related('market_pk')\
                .prefetch_related('category_fk')\
                .prefetch_related('product_option').filter(market_pk=market_id)
        else:
            product_list = Product.objects\
                .prefetch_related('market_pk')\
                .prefetch_related('category_fk')\
                .prefetch_related('product_option').all()
        serializer = ProductListSerializer(product_list, many=True)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)

    if request.method == 'POST':
        product_serializer = ProductPostSerializer(data=request.data)

        if product_serializer.is_valid():
            if market_yn:
                market_id = request.auth.payload['market_id']
                validate_data = product_serializer.validated_data
                if validate_data['market_pk'].id != market_id:
                    raise exceptions.APIException(detail={'code': ErrorMessage.MARKET_ID_NOT_CORRECT.code,
                                                          "message": ErrorMessage.MARKET_ID_NOT_CORRECT.message})
            product_serializer.save()
            response = BaseResponse(data=product_serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            if product_serializer.errors.get('market_pk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.MARKET_NOT_FOUND.code,
                                                  "message": ErrorMessage.MARKET_NOT_FOUND.message})
            if product_serializer.errors.get('category_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code,
                                                  "message": ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_VALIDATION_ERROR.code,
                                                         "message": ErrorMessage.PRODUCT_VALIDATION_ERROR.message})


@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes((IsAuthenticated,))
def product(request, product_id):
    # 사용자가  Market 인지 체크
    market_yn = request.auth.payload['market_yn']

    if request.method == 'GET':
        product_model = product_select(product_id)
        serializer = ProductListSerializer(product_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if request.method == 'PUT':
        product_model = product_select(product_id)
        serializer = ProductPutSerializer(product_model, data=request.data)
        if serializer.is_valid():
            if market_yn:
                market_id = request.auth.payload['market_id']
                validate_data = serializer.validated_data
                if validate_data['market_pk'].id != market_id:
                    raise exceptions.APIException(detail={'code': ErrorMessage.MARKET_ID_NOT_CORRECT.code,
                                                          "message": ErrorMessage.MARKET_ID_NOT_CORRECT.message})
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
        if market_yn:
            market_id = request.auth.payload['market_id']
            if product_model.market_pk.id != market_id:
                raise exceptions.APIException(detail={'code': ErrorMessage.MARKET_ID_NOT_CORRECT.code,
                                                      "message": ErrorMessage.MARKET_ID_NOT_CORRECT.message})
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
