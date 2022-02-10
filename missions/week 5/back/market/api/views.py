from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def markets(request):
    # 사용자가  Market 인지 체크
    method = request.method
    if method == 'GET':
        # TODO Market List
        return Response(data=None, status=status.HTTP_200_OK)

    if method == 'POST':
        # TODO Market Regist
        return Response(data=None, status=status.HTTP_201_CREATED)


@api_view(['PATCH', 'DELETE', 'GET'])
@permission_classes((IsAuthenticated,))
def market(request, market_id):
    method = request.method
    if method == 'GET':
        # TODO Market Detail
        return Response(data=None, status=status.HTTP_201_CREATED)
    if method == 'PATCH':
        # TODO Market Update
        return Response(data=None, status=status.HTTP_201_CREATED)
    if method == 'DELETE':
        # TODO Market Delete
        return Response(data=None, status=status.HTTP_200_OK)
