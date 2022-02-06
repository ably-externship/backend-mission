from product.models import Product, ProductDetail
from shop.models import Shop
# django rest api
from rest_framework import viewsets
from api.serializer import ProductSerializer, ProductDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.permissions import IsShopAdmin


# def token_decode(request):
#     jwt_object = JWTAuthentication()
#     header = jwt_object.get_header(request)
#     raw_token = jwt_object.get_raw_token(header)
#     validated_token = jwt_object.get_validated_token(raw_token)
#     user = jwt_object.get_user(validated_token)
#     return user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsShopAdmin,
    ]

    # 각 입점사별로 상품 목록을 보여줌
    def list(self, request, *args, **kwargs):
        user = request.user
        print("이것", request.user)
        try:
            shop_admin = Shop.objects.get(shop_id=user)
            queryset = Product.objects.filter(shop_id=shop_admin)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        except Shop.DoesNotExist:
            data = {
                'message': '입점사가 아닙니다. 입력하신 정보를 확인해주세요.'
            }
            return Response(data, status=404)
        except Product.DoesNotExist:
            data = {
                'message': '상품이 존재하지 않습니다.'
            }
            return Response(data, status=200)

    # 상품 등록
    def perform_create(self, serializer):
        shop_admin = Shop.objects.get(shop_id=self.request.user)
        serializer.save(shop_id=shop_admin)


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [
        IsAuthenticated,
        IsShopAdmin,
    ]

    def get_queryset(self):
        return ProductDetail.objects.filter(product_id=self.kwargs['product_pk'])

    # 상품 등록
    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs['product_pk'])
        serializer.save(product_id=product)