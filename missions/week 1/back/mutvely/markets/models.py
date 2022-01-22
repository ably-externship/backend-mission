from django.db import models

class Market(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    name = models.CharField('마켓이름', max_length=100)
    site_url = models.URLField('마켓사이트URL', max_length=100)
    email = models.EmailField('마켓대표이메일', max_length=100)


class ProductCategoryItem(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    name = models.CharField('이름', max_length=50)
  
  
class Product(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    is_deleted = models.BooleanField('삭제여부', default=False)
    delete_date = models.DateTimeField('삭제날짜', null=True, blank=True)

    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING)
    name = models.CharField('상품명(내부용)', max_length=100)
    display_name = models.CharField('상품명(노출용)', max_length=100)

    price = models.PositiveIntegerField('권장판매가')
    sale_price = models.PositiveIntegerField('실제판매가')

    is_hidden = models.BooleanField('노출여부', default=False)
    is_sold_out = models.BooleanField('품절여부', default=False)

    cate_item = models.ForeignKey(ProductCategoryItem, on_delete=models.DO_NOTHING)

    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰평점', default=0)


class Onepiece(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnePiece'


class Outwear(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Outwear'


class Pants(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pants'


class Skirt(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skirt'


class Top(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOP'


class Qna(models.Model):
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    prod_id = models.IntegerField()
    content = models.CharField(db_column='Content', max_length=300)  # Field name made lowercase.
    writer = models.CharField(max_length=20)
    title = models.CharField(db_column='Title', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QnA'

class Cart(models.Model):
    user_id = models.IntegerField()
    category = models.CharField(max_length=30)
    prod_id = models.IntegerField()
    prod_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Cart'

