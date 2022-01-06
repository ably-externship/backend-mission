from django.db import models
from django_mysql.models import ListTextField

# Create your models here.


class Product(models.Model):
    shop = models.ForeignKey('mall.Shop', on_delete=models.CASCADE, verbose_name='쇼핑몰') #1:N

    product_name = models.CharField(max_length=256, verbose_name='상품명')
    description = models.TextField(verbose_name='상품설명')

    price = models.IntegerField(verbose_name='상품가격')

    stock = models.IntegerField(verbose_name='재고') # option마다

    # image_urls = ListTextField(
    #     base_field=models.TextField(),
    #     size=100,  # Maximum of 100 imgUrls in list
    # ) #이미지 url, 여러개 ListField, ArrayField 안됨

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
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='쇼핑몰')

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
    productOptionGroup = models.ForeignKey(ProductOptionGroup, on_delete=models.CASCADE)
    optionItem = models.CharField(max_length=256, verbose_name='옵션내용')
    addPrice = models.IntegerField(default=0, verbose_name='추가 가격')  # 옵션 변경시 가격 변동, 주문 시
    stock = models.IntegerField(verbose_name='재고', default=0)

class ProductImg(models.Model):  # 이미지 여러개
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='쇼핑몰')
    img_url = models.TextField()


class ProductStock(models.Model):  # 이미지 여러개
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='쇼핑몰')
    productOptionGroup = models.ForeignKey(ProductOptionGroup, on_delete=models.CASCADE)
    productOptionGroup = models.ForeignKey(ProductOptionGroup, on_delete=models.CASCADE)
    stock = models.IntegerField()
