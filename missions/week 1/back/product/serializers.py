from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .pagination import LargeResultsSetPagination
from .models import Product, ProductOptionGroup, ProductOptionGroupItem, ProductImg, ProductReal
from mall.serializers import ShopSerializer

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = "__all__"

class ProductRealSerializer(ModelSerializer):
    pagination_class = LargeResultsSetPagination

    class Meta:
        model = ProductReal
        fields = ['id', 'reg_date', 'update_date', 'is_hidden', 'is_sold_out', 'product', 'option_1_display_name',
                  'option_1_name', 'option_2_display_name', 'option_2_name', 'add_price', 'stock_quantity', 'rgb_color']

class ProductRealCreateSerializer(ModelSerializer):
    pagination_class = LargeResultsSetPagination

    # 모델의 UniqueConstract 설정 덕분에 아래 작업을 안할 날이 곧 옵니다.
    # https://github.com/encode/django-rest-framework/issues/7173
    def validate(self, data):
        product = data.get('product', None)

        # 상품정보를 입력받을 때는 상품ID가 없는게 맞고
        # 상품정보를 저장할 때는 상품ID가 있다.
        if product and ProductReal.objects.filter(product=data['product'], option_1_name=data['option_1_name'],
                                                  option_2_name=data['option_2_name']).exists():
            raise serializers.ValidationError(
                {'error': 'product and option_1_name and option_2_name should be unique together'})
        return data

    class Meta:
        model = ProductReal
        fields = ['id', 'reg_date', 'update_date', 'is_hidden', 'is_sold_out', 'product', 'option_1_display_name',
                  'option_1_name', 'option_2_display_name', 'option_2_name', 'add_price', 'stock_quantity', 'rgb_color']
        extra_kwargs = {
            'product': {'required': False, 'allow_null': True},
        }

        # 이거 쓰면 입력시 product 를 필요로 함, 그런데 등록시에는 product를 알 수 없음..
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=model.objects.all(),
        #         fields=('product', 'option_1_name', 'option_2_name'),
        #         message="product and option_1_name and option_2_name should be unique together"
        #     )
        # ]



class ProductSerializer(serializers.ModelSerializer):
    imgs = ProductImgSerializer(many=True, read_only=True, source='productImgs')
    shop = ShopSerializer()
    product_reals = ProductRealSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'stock', 'register_date', 'status',
                  'imgs', 'shop', 'product_reals']


class ProductPatchSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'stock', 'register_date', 'status']


class ProductCreateSerializer(ModelSerializer):
    product_reals = ProductRealCreateSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id','product_name', 'description', 'price', 'stock', 'register_date', 'status','shop','product_reals']
                  #'imgs'


    @transaction.atomic #
    def create(self, validated_data):
        product_reals = validated_data.pop('product_reals', [])
        print("product_reals")
        print(product_reals)
        product = Product.objects.create(**validated_data)

        product_reals = list(map(lambda product_real: {**product_real, "product": product.id}, product_reals))

        for product_real in product_reals:
            product_real_serializer = ProductRealCreateSerializer(data=product_real)

            product_real_serializer.is_valid(raise_exception=True)
            product_real_serializer.save()

        return product


class ProductOptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroup
        fields = ('product','optionGroup','optionItems')

class ProductOptionGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionGroupItem
        fields = '__all__'

