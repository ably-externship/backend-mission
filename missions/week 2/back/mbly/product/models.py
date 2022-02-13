from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from market.models import Market
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField('카테고리 이름',max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=150) # 이름
    price = models.IntegerField() # 가격
    description = models.CharField(max_length=200) # 설명
    image = models.ImageField(upload_to='images/') # 이미지
    reg_date = models.DateTimeField(auto_now_add=True) # 등록일
    update_date = models.DateTimeField(auto_now=True) # 변경일
    market = models.ForeignKey(Market,on_delete=models.DO_NOTHING) # 마켓
    category = models.ForeignKey(ProductCategory,on_delete= models.DO_NOTHING) # 카테고리

    price = models.PositiveIntegerField('권장판매가')
    sale_price = models.PositiveIntegerField('실제판매가')

    is_deleted= models.BooleanField('삭제 여부',default = False)
    deleted_date = models.DateTimeField('삭제날짜',null = True,blank=True)
    is_hidden = models.BooleanField("숨김여부",default = False)
    hit_count = models.IntegerField('조회수',default=0)
    like_count = models.IntegerField('좋아요수',default=0)

    def is_sale(self):
        if self.price == self.sale_price:
            return False
        else:
            return True


    class Meta:
        ordering = ['-reg_date'] # 역순 정렬

class RealProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE) # 상품

    reg_date = models.DateTimeField(auto_now_add=True) # 등록일
    update_date = models.DateTimeField(auto_now=True) # 변경일
    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50)
    option_1_display_name = models.CharField('옵션1 이름(고객용)', max_length=50)
    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50)
    option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)

    is_sold_out = models.BooleanField('품절여부', default=False)
    is_hidden = models.BooleanField('노출여부', default=False)
    add_price = models.IntegerField('추가가격', default=0)
    stock_quantity = models.PositiveIntegerField('재고', default=0)  # 품절일때 유용함


class Question(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date'] # 역순 정렬

class Answer(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date'] # 역순 정렬