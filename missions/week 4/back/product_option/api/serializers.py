from rest_framework.serializers import ModelSerializer

from product_option.models import ProductOption
from rest_framework import serializers

from common.exception import ErrorMessage


class ProductOptionCreateSerializer(ModelSerializer):

    def validate(self, data):
        product = data.get('product', None)

        # 상품정보를 입력받을 때는 상품ID가 없는게 맞고
        # 상품정보를 저장할 때는 상품ID가 있다.
        if product and ProductOption.objects.filter(product=data['product'], size=data['size'],
                                                    color=data['color']).exists():
            raise serializers.ValidationError(
                detail={'code': ErrorMessage.PRODUCT_OPTION_DUPLICATE.code,
                        "message": ErrorMessage.PRODUCT_OPTION_DUPLICATE.message})
        return data

    class Meta:
        model = ProductOption
        fields = ['id', 'create_date', 'update_date', 'product_pk', 'size', 'color', 'sold_out_yn', 'add_price']
        extra_kwargs = {
            'product_pk': {'required': False, 'allow_null': True},
        }

        # 이거 쓰면 입력시 product 를 필요로 함, 그런데 등록시에는 product를 알 수 없음..
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=model.objects.all(),
        #         fields=('product', 'option_1_name', 'option_2_name'),
        #         message="product and option_1_name and option_2_name should be unique together"
        #     )
        # ]

class ProductOptionCreateSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = ['id', 'create_date', 'update_date', 'product_pk', 'size', 'color', 'sold_out_yn', 'add_price']
