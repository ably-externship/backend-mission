import datetime

from django.db.models import Case, When
from elasticsearch import Elasticsearch
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404

from accounts.apis.permissions import IsMarketAdmin
from .serializers import ProductSerializer, ProductOptionSerializer
from ..models import Product, ProductOption


class ProductViewSet(viewsets.ModelViewSet):
    class ElasticSearchFilter(filters.SearchFilter):
        def get_search_fields(self, view, request):
            pass

        def get_search_terms(self, request):
            params = request.query_params.get(self.search_param, '')
            params = params.replace('\x00', '')  # strip null characters
            params = params.replace(',', ' ')
            return params

        def filter_queryset(self, request, queryset, view):
            search_terms = self.get_search_terms(request)
            if not search_terms:
                return queryset
            queryset = self.search_by_elastic(search_terms)
            if not request.user.is_staff:
                queryset = queryset.filter(market=request.user.market)
            return queryset

        def search_by_elastic(self, keyword: str, min_price: int = 0, max_price: int = 1000000):
            elasticsearch = Elasticsearch('https://mbly.o-r.cc:9201', http_auth=('elastic', 'elasticpassword'))
            querystring = f"""
                SELECT
                id
                FROM mbly___products_product_type_2___v1
                WHERE (
                    MATCH (name_nori, '{keyword}')
                    OR
                    MATCH (display_name_nori, '{keyword}')
                    OR
                    MATCH (detail_nori, '{keyword}')
                    OR
                    MATCH (category_name_nori, '{keyword}')
                    OR
                    MATCH (market_name_nori, '{keyword}')
                ) AND discounted_price BETWEEN {min_price} AND {max_price}
                ORDER BY score() DESC
                """
            response = elasticsearch.sql.query(body={"query": querystring})
            product_ids = [row[0] for row in response['rows']]
            order = Case(*[When(id=id, then=pos) for pos, id in enumerate(product_ids)])
            queryset = Product.objects.filter(id__in=product_ids).order_by(order)
            return queryset

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [ElasticSearchFilter]

    def get_queryset(self):
        return Product.objects.filter(deleted=False) if self.request.user.is_staff else Product.objects.filter(
            market=self.request.user.market, deleted=False)

    def get_permissions(self):
        return [permission() for permission in
                ([permissions.IsAdminUser] if self.request.user.is_staff else [IsMarketAdmin])]

    def perform_create(self, serializer):
        market = self.request.user.market
        serializer.save(market=market)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.deleted_at = datetime.datetime.now(datetime.timezone.utc)
        instance.save()


class ProductOptionViewSet(viewsets.ModelViewSet):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProductOption.objects.filter(product=self.get_product())

    def get_permissions(self):
        class ProductOptionPermission(permissions.BasePermission):
            def has_permission(self, request, view):
                product = get_object_or_404(Product, pk=view.kwargs['product_pk'])
                return request.user.market == product.market

        return [permission() for permission in
                ([permissions.IsAdminUser] if self.request.user.is_staff else [IsMarketAdmin, ProductOptionPermission])]

    def perform_create(self, serializer):
        serializer.save(product=self.get_product())

    def get_product(self):
        product_pk = self.kwargs['product_pk']
        user = self.request.user
        return get_object_or_404(Product, pk=product_pk) if user.is_staff else get_object_or_404(Product, pk=product_pk,
                                                                                                 market=user.market)
