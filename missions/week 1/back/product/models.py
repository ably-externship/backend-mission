from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint


class Product(models.Model):
    shop = models.ForeignKey('mall.Shop', on_delete=models.CASCADE, verbose_name='쇼핑몰') #1:N

    product_name = models.CharField(max_length=256, verbose_name='상품명')
    description = models.TextField(verbose_name='상품설명')

    price = models.IntegerField(verbose_name='상품가격')

    stock = models.IntegerField(verbose_name='재고') # 전체 - option 그룹 1에서 전체 재고 확인, 부분 품절 - OptionGroup 마다 재고 확인

    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    status = models.CharField(choices=(
        ('sale', 'sale'),
        ('품절', 'out of stock')
        ),  default="sale", max_length=32, verbose_name='상태')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'
        verbose_name = '상품'
        verbose_name_plural = '상품'

    def calculatePrice(self, price=0):
        self.price += price

    def calculateStock(self, stock=0):
        self.stock += stock


    #ProductOptionGroupItem, ProductOptionGroup
    #
    #부분 품절
    #전체 품절



class ProductOptionGroup(models.Model):  # 색상, 사이즈
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='optionGroups')

    optionGroup = models.CharField(max_length=256, verbose_name='옵션그룹')
    # description = models.TextField(verbose_name='옵션 설명')
    # 등록 날짜

    # def __str__(self):
    #     return self.optionGroup

    # class Meta:
    #     db_table = 'optionGroups'
    #     verbose_name = '상품옵션'
    #     verbose_name_plural = '상품옵션'

class ProductOptionGroupItem(models.Model):  # red, black, 55, 66
    productOptionGroup = models.ForeignKey(ProductOptionGroup, on_delete=models.CASCADE,related_name='optionItems')
    addPrice = models.IntegerField(default=0, verbose_name='추가 가격')  # 옵션 변경시 가격 변동, 주문 시
    stock = models.IntegerField(verbose_name='재고', default=0)

class ProductImg(models.Model):  # 이미지 여러개
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productImgs')
    img_url = models.TextField()
    def __str__(self):
        return self.img_url

class ProductStock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productStocks')
    productOptionGroup = models.ForeignKey(ProductOptionGroup, on_delete=models.CASCADE)
    ProductOptionGroupItem = models.ForeignKey(ProductOptionGroupItem, on_delete=models.CASCADE)
    stock = models.IntegerField()



class ProductReal(models.Model):
    def __str__(self):
        return f"{self.id}, {self.option_1_display_name} / {self.option_2_display_name}"

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_reals")
    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50)
    option_1_display_name = models.CharField('옵션1 이름(고객용)', max_length=50)
    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50)
    option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)
    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름(내부용)', max_length=50, default='', blank=True)
    option_3_display_name = models.CharField('옵션3 이름(고객용)', max_length=50, default='', blank=True)
    is_sold_out = models.BooleanField('품절여부', default=False)
    is_hidden = models.BooleanField('숨김여부', default=False)
    add_price = models.IntegerField('추가가격', default=0)
    stock_quantity = models.PositiveIntegerField('재고개수', default=0)  # 품절일때 유용함

    # class Meta:   #
    #     constraints = [
    #         UniqueConstraint(
    #             'product',
    #             'option_1_name',
    #             'option_2_name',
    #             'option_3_name',
    #             name='option_name_unique',
    #         ),
    #     ]

    @property
    def rgb_color(self):
        return ProductReal.rgb_color_from_color_name(self.option_2_name)

    @classmethod
    def rgb_color_from_color_name(cls, color):
        if color == '레드':
            rgb_color = 'FF0000'
        elif color == '그린':
            rgb_color = '008000'
        elif color == '블루':
            rgb_color = '0000FF'
        elif color == '핑크':
            rgb_color = 'ffc0cb'
        elif color == '와인':
            rgb_color = '722F37'
        else:
            rgb_color = 'FFFFFF'

        return rgb_color
