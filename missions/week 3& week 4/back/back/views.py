from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def validate_jwt_token(request):

    try:
        token = request.META['HTTP_AUTHORIZATION']
        data = {'token': token.split()[1]}
        valid_data = TokenVerifySerializer().validate(data)
    except Exception as e:
        return Response(e)

    return Response(status=status.HTTP_200_OK)