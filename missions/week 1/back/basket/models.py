from django.db import models

# Create your models here.


#사용자 JWT를 받아

class Basket(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')


    #Option의 경우 1) 테이블 따로 2) 컬럼 으로  -> 더 현실적

    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50, default='', blank=True)
    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50, default='', blank=True)
    #option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)
    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름(내부용)', max_length=50, default='', blank=True)
    #option_3_display_name = models.CharField('옵션3 이름(고객용)', max_length=50, default='', blank=True)

    price = models.IntegerField(default=0, blank=False)

    #productOption = models.ForeignKey('product.ProductOptionGroup', on_delete=models.CASCADE, verbose_name='상품옵션')
    #productOptionItem = models.ForeignKey('product.ProductOptionGroupItem' , on_delete=models.CASCADE, verbose_name='상품옵션선택')

    user = models.ForeignKey('lionuser.Lionuser', on_delete=models.CASCADE, verbose_name='사용자')

    count = models.IntegerField()

#주문 생성하기 주문 삭제하기

#재고확인



