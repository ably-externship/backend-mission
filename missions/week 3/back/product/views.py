from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *

# 제품 리스트
@api_view(['GET'])
def ProductList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

# 제품 추가
@api_view(['POST'])
def ProductCreate(request):
    serializer = ProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("에러 코드 :",serializer.errors)

    return Response(serializer.data)

# 제품 상세
@api_view(['GET'])
def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializer(product, many=False)

    return Response(serializer.data)

# 제품 수정
@api_view(['PUT'])
def ProductUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductUpdateSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Deleted')


# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductCreate(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductCreateSerializer
#
# class ProductUpdate(UpdateAPIView):
#     lookup_field = 'no'
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductDelete(DestroyAPIView):
#     lookup_field = 'no'
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductDetail(RetrieveAPIView):
#     lookup_field = 'no'
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer



