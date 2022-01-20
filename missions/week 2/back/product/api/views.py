from rest_framework.decorators import api_view

from common.BaseResponse import BaseResponse
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def test_api(request):
    # raise exceptions.APIException(detail={'code': ErrorMessage.PRODUCT_001.code, "message":ErrorMessage.PRODUCT_001.message})
    response = BaseResponse(data=["aaa","bbb","CCC"], message="AAA", code="SUCCESS")
    return Response(data=response.to_dict(), status=status.HTTP_200_OK)
