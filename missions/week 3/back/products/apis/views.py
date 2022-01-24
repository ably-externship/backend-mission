import datetime

from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404

from accounts.apis.permissions import IsMarketAdmin
from .serializers import ProductSerializer, ProductOptionSerializer
from ..models import Product, ProductOption


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsMarketAdmin]

    def get_queryset(self):
        return Product.objects.filter(market=self.request.user.market, deleted=False)

    def perform_create(self, serializer):
        market = self.request.user.market
        serializer.save(market=market)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.deleted_at = datetime.datetime.now(datetime.timezone.utc)
        instance.save()


class ProductOptionViewSet(viewsets.ModelViewSet):
    class ProductOptionPermission(permissions.BasePermission):
        def has_permission(self, request, view):
            product = get_object_or_404(Product, pk=view.kwargs['product_pk'])
            return request.user.market == product.market

    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsMarketAdmin, ProductOptionPermission]

    def get_queryset(self):
        return ProductOption.objects.filter(product=self.get_product())

    def perform_create(self, serializer):
        serializer.save(product=self.get_product())

    def get_product(self):
        return get_object_or_404(Product, pk=self.kwargs['product_pk'], market=self.request.user.market)
