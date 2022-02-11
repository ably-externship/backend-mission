from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


# 장바구니 관련
# 장바구니 리스트
@api_view(['GET'])
def CartList(request):
    user_id=request.user.id
    Carts = Cart.objects.select_related('product').select_related('product_option').filter(user=user_id)
    serializer = CartSerializer(Carts, many=True)

    return Response(serializer.data)



# 장바구니 삭제
@api_view(['DELETE'])
def CartDelete(request, pk):
    cart = Cart.objects.get(id=pk)
    # serializer = CartSerializer(cart)
    cart.delete()

    return Response('Deleted')



# 장바구니 수정
@api_view(['PATCH'])
def CartUpdate(request, pk):
    cart = Cart.objects.get(id=pk)
    serializer = CartSerializer(instance=cart, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



# 장바구니 추가
@api_view(['POST'])
def CartCreate(request):
    serializer = CartCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("에러 코드 :", serializer.errors)

    return Response(serializer.data)
