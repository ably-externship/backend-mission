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

# 제품 삭제
@api_view(['DELETE'])
def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Deleted')


# 제품 찾기
@api_view(['GET'])
def ProductFind(request, name):
    product = Product.objects.get(name=name)
    product_id = product.id
    serializer = ProductFindSerializer(product)

    return Response(serializer.data)




# 옵션 리스트
@api_view(['GET'])
def OptionList(request):
    options = Product_option.objects.all()
    serializer = OptionSerializer(options, many=True)

    return Response(serializer.data)


# 옵션 추가
@api_view(['POST'])
def OptionCreate(request):
    serializer = OptionCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("에러 코드 :",serializer.errors)

    return Response(serializer.data)


