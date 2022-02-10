from django.db import models
from core.models import TimeStampedModel
from accounts.models import Seller

# Create your models here.


class MainCategory(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='메인카테고리')
    
    class Meta:
        verbose_name_plural = '1. 메인카테고리 목록'
        db_table = 'maincategories'
    
    def __str__(self):
        return str(self.id)


class SubCategory(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name='메인카테고리', related_name='subcategory')
    name = models.CharField(max_length=20, verbose_name='서브카테고리')
    
    class Meta:
        verbose_name_plural = '2. 서브카테고리 목록'
        db_table = 'subcategories'
    
    def __str__(self):
        return str(self.id)


class BaseMerchandise(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, verbose_name='서브카테고리', related_name='basemerchandise')
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, verbose_name='셀러', related_name='basemerchandise')
    common_code = models.CharField(max_length=8, verbose_name='상품 공통코드')
    name = models.CharField(max_length=20, verbose_name='상품명')
    standard_price = models.PositiveIntegerField(default=0, verbose_name='상품 정가')
    discounted_price = models.PositiveIntegerField(default=0, verbose_name='상품 할인금액')
    main_img = models.URLField(blank=True, null=True, verbose_name='상품 메인이미지')
    sub_img_0 = models.URLField(blank=True, null=True, verbose_name='상품 서브이미지0')
    sub_img_1 = models.URLField(blank=True, null=True, verbose_name='상품 서브이미지1')
    sub_img_2 = models.URLField(blank=True, null=True, verbose_name='상품 서브이미지2')
    description = models.TextField(blank=True, null=True, verbose_name='상품 설명')
    
    class Meta:
        verbose_name_plural = '3. 상품 목록'
        db_table = 'basemerchandises'
    
    def __str__(self):
        return str(self.id)


class Merchandise(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    basemerchandise = models.ForeignKey(BaseMerchandise, on_delete=models.CASCADE, null=True, verbose_name='상품', related_name='merchandise')
    full_code = models.CharField(max_length=12, verbose_name='옵션상품 전체코드')
    color = models.CharField(max_length=20, verbose_name='옵션상품 색상')
    size = models.CharField(max_length=6,
        choices=(
            ('FREE', 'FREE'),
            ('SMALL', 'S'),
            ('MEDIUM', 'M'),
            ('LARGE', 'L'),
            ('XLARGE', 'XL')
        ),
        verbose_name='옵션상품 사이즈'
    )
    current_stock = models.PositiveIntegerField(default=0, verbose_name='옵션상품 현재재고')
    safety_stock = models.PositiveIntegerField(default=0, verbose_name='옵션상품 안전재고')
    soldout_state = models.CharField(max_length=3,
        choices=(
            ('IN', 'INSTOCK'),
            ('TEM', 'TEMPORARY_SOLDOUT'),
            ('PER', 'PERMANANT_SOLDOUT'),
        ),
        verbose_name='옵션상품 품절상태'
    )
    on_sale = models.BooleanField(default=True, verbose_name='상품 판매')
    on_display = models.BooleanField(default=True, verbose_name='상품 전시')
    
    class Meta:
        verbose_name_plural = '4. 옵션상품 목록'
        db_table = 'merchandises'
    
    def __str__(self):
        return str(self.id)