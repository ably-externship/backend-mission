from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.views import TokenObtainPairView

from common.BaseResponse import BaseResponse
from users.api.serializers import UserAuthSerializer, UserAuthResponseSerializer, UserAuthResponse, \
    MyTokenObtainPairSerializer
from rest_framework import exceptions, status

from rest_framework.response import Response
import uuid

from users.models import RefreshStorage, User

from rest_framework_simplejwt.exceptions import TokenError


@csrf_exempt
@api_view(['POST'])
def get_token(request):
    user = UserAuthSerializer(request.data).data
    user_auth = authenticate(username=user.get('username'), password=user.get('password'))
    if user_auth is not None:
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
