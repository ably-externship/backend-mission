from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from common.BaseResponse import BaseResponse
from users.api.serializers import UserAuthSerializer, UserAuthResponseSerializer, UserAuthResponse
from rest_framework import exceptions, status

from rest_framework.response import Response
import uuid

from users.models import RefreshStorage


@csrf_exempt
@api_view(['POST'])
def get_token(request):
    user = UserAuthSerializer(request.data).data
    user_auth = authenticate(username=user.get('username'), password=user.get('password'))
    if user_auth is not None:
        refresh = RefreshToken.for_user(user_auth)

        hash_value = uuid.uuid4()

        RefreshStorage.objects.create(hash_value=hash_value, refresh_token=str(refresh), user_fk=user_auth)
        response_data = BaseResponse(data=str(refresh.access_token), message=None, code="SUCCESS")

        response = Response(data=response_data.to_dict(), status=status.HTTP_200_OK)
        response.set_cookie(key='refresh_hash', value=hash_value, httponly=True)
        return response
    else:
        raise exceptions.AuthenticationFailed(detail=None, code=None)


@api_view(['GET'])
def refresh_token(request):
    #TODO Refresh-Token 처리
    refresh_hash = request.COOKIES['refresh_hash']
    refresh_storage = RefreshStorage.objects.get(hash_value=refresh_hash)
    return Response(data=None, status=status.HTTP_200_OK)

