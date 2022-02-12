import uuid

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import exceptions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from common.BaseResponse import BaseResponse
from market.models import Market
from users.api.serializers import UserAuthSerializer, MyTokenObtainPairSerializer
from users.models import RefreshStorage, User


@csrf_exempt
@api_view(['POST'])
def get_token(request):
    user = UserAuthSerializer(request.data).data
    user_auth = authenticate(username=user.get('username'), password=user.get('password'))
    if user_auth is not None:
        if user_auth.market_yn:
            user_auth.market_info = Market.objects.get(user_fk=user_auth.id)
        return issued_token(user_auth)
    else:
        raise exceptions.AuthenticationFailed(detail=None, code=None)


@api_view(['GET'])
def refresh_token(request):
    refresh_hash = request.COOKIES['refresh_hash']

    try:
        refresh_storage = RefreshStorage.objects.get(hash_value=refresh_hash)
        token = RefreshToken(refresh_storage.refresh_token)

        user = User.objects.get(id=token['user_id'])
        if user is not None:
            if user.market_yn:
                user.market_info = Market.objects.get(user_fk=user.id)

        return issued_token(user)
    except TokenError as e:
        raise exceptions.AuthenticationFailed(detail=None, code=None)


# 토큰 발급 처리
def issued_token(user_info):
    refresh = MyTokenObtainPairSerializer.get_token(user_info)
    hash_value = uuid.uuid4()
    RefreshStorage.objects.create(hash_value=hash_value, refresh_token=str(refresh), user_fk=user_info)
    response_data = BaseResponse(data=str(refresh.access_token), message=None, code="SUCCESS")
    response = Response(data=response_data.to_dict(), status=status.HTTP_200_OK)
    response.set_cookie(key='refresh_hash', value=hash_value, httponly=True)
    return response
