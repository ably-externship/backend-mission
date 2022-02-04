from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.core.paginator import Paginator


from .models import Product, ProductImg, ProductReal
from .serializers import ProductSerializer, ProductImgSerializer, ProductCreateSerializer, ProductPatchSerializer, \
    ProductRealSerializer, ProductRealCreateSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, generics

from rest_framework.permissions import IsAdminUser

from elasticsearch import Elasticsearch
from django.db.models import Prefetch, Case, When



@csrf_exempt
def itemIndex(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return render(request, 'ALLproduct.html', {'product_list': posts})

@csrf_exempt
def allItem(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def itemSearch(request):
    if request.method == 'POST':
        item_search = request.POST.get('item_search')
        result = Product.objects.filter(product_name__contains=item_search)

        serializer = ProductSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)



from django.utils.deprecation import MiddlewareMixin

class DisableCsrfCheck(MiddlewareMixin):

    def process_request(self, req):
        attr = '_dont_enforce_csrf_checks'
        if not getattr(req, attr, False):
            setattr(req, attr, True)


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')

# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JWTAuthentication,))
class BillingRecordsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   # pagination_class = DashboardPageNumberPagination


class ProductViewSet(viewsets.ViewSet):

    @csrf_exempt
    def list(self, request):  # /api/shop
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/shop
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @csrf_exempt
    def retrieve(self, request, pk=None):  # /api/shop/<pk>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductImgViewSet(viewsets.ViewSet):
    @csrf_exempt
    def list(self, request):  # /api/shop

        product = ProductImg.objects.all()
        serializer = ProductImgSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/shop
        serializer = ProductImgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @csrf_exempt
    def retrieve(self, request, pk=None):  # pk  product , many
        product = ProductImg.objects.get(product=pk)
        serializer = ProductImgSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = ProductImg.objects.get(id=pk)
        serializer = ProductImgSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = ProductImg.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#마켓 관리자 CRUD
class MarketAdminProductListCreateView(ListCreateAPIView):
    #인증 후
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        shop = user.shop.id
        print("관리자 shop Id : ", shop)
        return Product \
            .objects \
            .prefetch_related('shop') \
            .prefetch_related('product_reals') \
            .filter(shop=shop)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        else:
            return ProductCreateSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #
    #     return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        shop = self.request.user.shop.id
        request.data.update({'shop': shop})
        print(request.data)
        return super().create(request, *args, **kwargs)


# MarketAdmin 용 상품 단건조회, 수정(PATCH), 삭제 처리 뷰
class MarketAdminProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # 인증 후
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] #IsAuthenticated IsAdminUser

    # 일부러 PUT을 없애기 위해
    allowed_methods = ('GET', 'PATCH', 'DELETE', 'OPTION')

    # N+1
    # 마켓관리자의 관리 쇼핑몰 상품만
    def get_queryset(self):
        user = self.request.user
        shop = user.shop.id
        print("관리자 shop Id : ", shop)

        return Product \
            .objects \
            .prefetch_related('shop') \
            .prefetch_related('product_reals') \
            .filter(shop=shop)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        else:
            return ProductPatchSerializer



class MarketAdminApiProductRealListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser] #IsAuthenticated

    def create(self, request, *args, **kwargs):
        request.data.update({'product': kwargs['product_id']})
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        product_id = self.kwargs['product_id']

        return ProductReal \
            .objects \
            .filter(product=product_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductRealSerializer
        else:
            return ProductRealCreateSerializer

# @require_GET
@csrf_exempt
def search_by_elastic(request):
    keyword, min_price, max_price = "소녀시대", 100, 1000000
    print(keyword)

    elasticsearch = Elasticsearch(
        "http://54.180.100.75:9200", http_auth=('elastic', 'changeme'), )

    elastic_sql = f"""
        SELECT
        id
        FROM
        mega_market___products_product_type_2___v1
        WHERE
        (
            MATCH(name_nori, '{keyword}')
            OR
            MATCH(display_name_nori, '{keyword}')
            OR
            MATCH(description_nori, '{keyword}')
            OR
            MATCH(cate_item_name_nori, '{keyword}')
            OR
            MATCH(market_name_nori, '{keyword}')
        )
        AND sale_price BETWEEN {min_price} AND {max_price}
        ORDER BY score() DESC
    """

    elastic_sql = f"""
              SELECT * FROM mega_market___products_product_type_2___v1
        """

    response = elasticsearch.sql.query(body={"query": elastic_sql})

    product_ids = [row[3] for row in response['rows']]
    print(product_ids)

    order = Case(*[When(id=id, then=pos) for pos, id in enumerate(product_ids)])

    queryset = Product.objects.filter(id__in=product_ids).order_by(order)

    return HttpResponse(queryset)
