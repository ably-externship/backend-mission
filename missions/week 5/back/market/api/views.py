from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.BaseResponse import BaseResponse
from market.api.serializers import MarketCreateSerializer, MarketListSerializer, MarketSelectSerializer, \
    MarketPatchSerializer
from rest_framework import exceptions

from common.exception.ErrorMessage import ErrorMessage
from market.models import Market


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def markets(request):
    # 사용자가  Market 인지 체크
    method = request.method
    if method == 'GET':
        market_list = Market.objects.all()
        serializer = MarketListSerializer(market_list, many=True)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)

    if method == 'POST':
        market_serializer = MarketCreateSerializer(data=request.data)
        if market_serializer.is_valid():
            market_serializer.save()
            response = BaseResponse(data=market_serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            if market_serializer.errors.get('user_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.USER_NOT_FOUND.code,
                                                  "message": ErrorMessage.USER_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.MARKET_VALIDATION_ERROR.code,
                                                         "message": ErrorMessage.MARKET_VALIDATION_ERROR.message})


@api_view(['PATCH', 'DELETE', 'GET'])
@permission_classes((IsAuthenticated,))
def market(request, market_id):
    method = request.method
    if method == 'GET':
        market_model = market_select(market_id)
        serializer = MarketSelectSerializer(market_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if method == 'PATCH':
        market_model = market_select(market_id)
        market_serializer = MarketPatchSerializer(market_model, data=request.data)
        if market_serializer.is_valid():
            market_serializer.save()
            response = BaseResponse(data=market_serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            if market_serializer.errors.get('user_fk') is not None:
                raise exceptions.NotFound(detail={'code': ErrorMessage.USER_NOT_FOUND.code,
                                                  "message": ErrorMessage.USER_NOT_FOUND.message})
            else:
                raise exceptions.ValidationError(detail={'code': ErrorMessage.MARKET_VALIDATION_ERROR.code,
                                                         "message": ErrorMessage.MARKET_VALIDATION_ERROR.message})
    if method == 'DELETE':
        market_model = market_select(market_id)
        market_model.market_status = 'DEACTIVE'
        market_model.save()
        serializer = MarketPatchSerializer(market_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)


def market_select(market_id):
    try:
        market_model = Market.objects.select_related('user_fk').get(id=market_id)
        return market_model
    except Market.DoesNotExist:
        raise exceptions.NotFound(
            detail={'code': ErrorMessage.MARKET_NOT_FOUND.code, "message": ErrorMessage.MARKET_NOT_FOUND.message})
