from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.api.serializers import ProductSerializer
from product.models import Product, CartItem


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    


# TODO: Django 의 Request 객체 vs DRF 의 Request 객체
# django.core.handlers.wsgi.WSGIRequest
# rest_framework.request.Request

# @api_view(['POST'])
# def change_quantity_api_view(request):
#
#     cart_item_id = request.data.get('id')
#     quantity = request.data.get('quantity')
#
#     cart_item = CartItem.objects.get(user=request.user, id=cart_item_id)
#     cart_item.quantity = quantity
#     cart_item.save()
#
#     return Response(status=status.HTTP_200_OK)

#
# def cart_delete_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data)
#
#         cart_item = CartItem.objects.get(user=request.user, id=data.get('id'))
#         cart_item.delete()
#
#     return JsonResponse(data)
