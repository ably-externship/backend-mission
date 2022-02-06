from distutils.command.upload import upload
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

from vendors.models import Vendor


class Product(models.Model):
    vendor = models.ForeignKey(
        Vendor, null=True, blank=True, on_delete=models.CASCADE)        # vendor_id
    name = models.CharField(max_length=128)                             # 제품명
    price = models.IntegerField(
        null=True)                                       # 가격
    sale_price = models.IntegerField(
        null=True)                                  # 세일 가격
    description = models.TextField()                                    # 제품 설명
    image = models.ImageField(upload_to='img/', null=True)              # 이미지
    image_detail = models.ImageField(
        upload_to='img/', null=True)       # 상세 이미지

    is_deleted = models.BooleanField(default=False)                     # 삭제 여부
    deleted_date = models.DateTimeField(
        auto_now=True, verbose_name="삭제 날짜")                           # 삭제 날짜
    is_hidden = models.BooleanField(
        default=False)                       # 숨김 여부
    is_sold_out = models.BooleanField(
        default=False)                     # 품절 여부
    hit_count = models.IntegerField(verbose_name='조회수', default=0)      # 조회 수
    like_count = models.IntegerField(verbose_name='좋아요수', default=0)    # 좋아요 수
    reg_date = models.DateTimeField(
        auto_now=True, verbose_name='등록일')   # 등록 날짜
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='등록일')                               # 갱신 날짜

    quantity = models.IntegerField(default=0)                             # 수량

    def __str__(self):
        return '{} {}'.format(self.name, self.reg_date)


class ProductOption(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)  # product_id

    reg_date = models.DateTimeField(
        auto_now=True, verbose_name='등록일')                               # 등록날짜
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='등록일')                            # 갱신날짜

    option1_type = models.CharField(
        max_length=128, verbose_name='옵션1 유형')                             # 옵션1 유형
    option1_name = models.CharField(
        max_length=128, verbose_name='옵션1 이름')                             # 옵션1 이름
    option1_price = models.IntegerField(
        verbose_name='옵션1 추가가격', default=0)                           # 옵션1 추가가격
    option1_stock = models.IntegerField(
        verbose_name='옵션1 재고수량')                                      # 옵션1 재고수량

    option2_type = models.CharField(
        max_length=128, null=True, verbose_name='옵션2 유형', default=None)    # 옵션2 유형
    option2_name = models.CharField(
        max_length=128, null=True, verbose_name='옵션2 유형', default=None)    # 옵션2 이름
    option2_price = models.IntegerField(
        null=True, verbose_name='옵션2 추가가격', default=None)             # 옵션2 추가가격
    option2_stock = models.IntegerField(
        null=True, verbose_name='옵션2 재고수량', default=None)             # 옵션2 재고수량


class ProductCategory(models.Model):
    name = models.CharField(max_length=16)
