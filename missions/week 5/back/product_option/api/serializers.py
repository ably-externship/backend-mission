from rest_framework.serializers import ModelSerializer

from product_option.models import ProductOption
from rest_framework import serializers

from common.exception import ErrorMessage


class ProductOptionCreateSerializer(ModelSerializer):

    def validate(self, data):
        product = data.get('product', None)

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

class ProductOptionDetailSerializer(ModelSerializer):

    class Meta:
        model = ProductOption
        fields = ['id', 'create_date', 'update_date', 'product_pk', 'size', 'color', 'sold_out_yn', 'add_price']
