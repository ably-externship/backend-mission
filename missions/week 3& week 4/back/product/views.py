from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.http import JsonResponse
from django.db.models import Prefetch, Case, When
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from elasticsearch import Elasticsearch

# 제품 리스트
@api_view(['GET'])
def ProductList(request):

    # ElasticSearch 검색 엔진
    if request.query_params['search']:
        keyword = request.query_params['search']

        elasticsearch = Elasticsearch(
            "http://192.168.56.101:9200", http_auth=('elastic', 'elasticpassword'), )

        elastic_sql = f"""
            SELECT
            id
            FROM
            mall___product_product_type_1___v1
            WHERE
            (
            MATCH(name_nori, '{keyword}')
            OR
            MATCH(category_nori, '{keyword}')
            OR
            MATCH(description_nori, '{keyword}')
            )
            ORDER BY score() DESC
        """

        response = elasticsearch.sql.query(body={"query": elastic_sql})
        product_ids = [row[0] for row in response['rows']]
        order = Case(*[When(id=id, then=pos) for pos, id in enumerate(product_ids)])
        queryset = Product.objects.filter(id__in=product_ids).order_by(order)
    else:
        queryset = Product.objects

    user_id = request.user.id
    products = queryset.prefetch_related('product_options').filter(market=user_id)
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
@api_view(['PATCH'])
def ProductUpdate(request, pk):
    user_id = request.user.id
    product = Product.objects.get(id=pk)

    if product.market_id==user_id:
        serializer = ProductUpdateSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print("에러 코드 :",serializer.errors)

        return Response(serializer.data)
    else:
        return JsonResponse({'message' : 'INVALID TOKEN'}, status = 403)

# 제품 삭제
@api_view(['DELETE'])
def ProductDelete(request, pk):
    user_id = request.user.id
    product = Product.objects.get(id=pk)

    if product.market_id == user_id:
        product.delete()
        return Response('Deleted')
    else:
        return JsonResponse({'message': 'INVALID TOKEN'}, status=403)


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


# ElasticSearch 테스트용
@api_view(['GET'])
def search_by_elastic(request: HttpRequest):
    keyword, min_price, max_price = "청바지", 100, 1000000

    elasticsearch = Elasticsearch(
        "http://192.168.56.101:9200", http_auth=('elastic', 'elasticpassword'), )

    elastic_sql = f"""
        SELECT
        id
        FROM
        mall___product_product_type_1___v1
        WHERE
        (
        MATCH(name_nori, '{keyword}')
        OR
        MATCH(category_nori, '{keyword}')
        OR
        MATCH(description_nori, '{keyword}')
        )
        ORDER BY score() DESC
    """

    response = elasticsearch.sql.query(body={"query": elastic_sql})
    product_ids = [row[0] for row in response['rows']]
    order = Case(*[When(id=id, then=pos) for pos, id in enumerate(product_ids)])
    queryset = Product.objects.filter(id__in=product_ids).order_by(order)

    return HttpResponse(queryset)
