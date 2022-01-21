from rest_framework.decorators import api_view

from common.BaseResponse import BaseResponse
from rest_framework.response import Response
from rest_framework import status

from product.api.serializers import ProductSerializer
from product.models import Product


@api_view(['GET'])
def test_api(request):
    # raise exceptions.APIException(detail={'code': ErrorMessage.PRODUCT_001.code, "message":ErrorMessage.PRODUCT_001.message})
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    response = BaseResponse(data=serializer.data, message="AAA", code="SUCCESS")
    return Response(data=response.to_dict(), status=status.HTTP_200_OK)
