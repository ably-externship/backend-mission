from django.views.decorators.csrf import csrf_exempt
from rest_framework import exceptions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.BaseResponse import BaseResponse
from common.exception.ErrorMessage import ErrorMessage
from product_category.api.serializers import ProductCategorySerializer
from product_category.models import ProductCategory


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def product_categorys(request):
    method = request.method
    if method == 'GET':
        product_category_list = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(product_category_list, many=True)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)

    if method == 'POST':
        product_category_serializer = ProductCategorySerializer(data=request.data)
        if product_category_serializer.is_valid():
            product_category_serializer.save()
            response = BaseResponse(data=product_category_serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_CATEGORY_INVALID.code,
                                                         "message": ErrorMessage.PRODUCT_CATEGORY_INVALID.message})


@api_view(['PATCH', 'DELETE', 'GET'])
@permission_classes((IsAuthenticated,))
def product_category(request, category_id):
    method = request.method
    if method == 'GET':
        category_model = category_select(category_id)
        serializer = ProductCategorySerializer(category_model)
        response = BaseResponse(data=serializer.data, message=None, code="SUCCESS")
        return Response(data=response.to_dict(), status=status.HTTP_200_OK)
    if method == 'PATCH':
        category_model = category_select(category_id)
        category_serializer = ProductCategorySerializer(category_model, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            response = BaseResponse(data=category_serializer.data, message=None, code="SUCCESS")
            return Response(data=response.to_dict(), status=status.HTTP_201_CREATED)
        else:
            raise exceptions.ValidationError(detail={'code': ErrorMessage.PRODUCT_CATEGORY_INVALID.code,
                                                         "message": ErrorMessage.PRODUCT_CATEGORY_INVALID.message})
    if method == 'DELETE':
        category_model = category_select(category_id)
        category_model.category_status = 'DEACTIVE'
        category_model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


def category_select(category_id):
    try:
        product_category_model = ProductCategory.objects.get(id=category_id)
        return product_category_model
    except ProductCategory.DoesNotExist:
        raise exceptions.NotFound(
            detail={'code': ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.code, "message": ErrorMessage.PRODUCT_CATEGORY_NOT_FOUND.message})
