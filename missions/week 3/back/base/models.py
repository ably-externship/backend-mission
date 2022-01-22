from django.db import models
from django.utils import timezone 
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class MallsList(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('마켓이름', max_length=100)
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)


class MallsQuestion(models.Model):
    q_num = models.AutoField(primary_key=True)
    author = models.ForeignKey('accounts.User', models.DO_NOTHING) # 작성자명
    title = models.CharField(max_length=200) # 제목, 길이제한 O
    text = models.TextField() # 내용, 길이제한 X
    reply = models.CharField(max_length=1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now) # 최초생성시각
    published_date = models.DateTimeField( '발행날짜',blank=True, null=True) # 발행날짜

    def published_date(self): # 발행
        self.published_date = timezone.now() # 현재시각 저장
        self.save()



class MallsAnswer(models.Model):
    q_num = models.ForeignKey('MallsQuestion', models.DO_NOTHING, db_column='q_num')
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    answer = models.TextField() # 내용, 길이제한 X


class Category(models.Model):
    name = models.CharField('카테고리', max_length=50)


class MallsItem(models.Model):
    id = models.ForeignKey('MallsList', models.DO_NOTHING, db_column='id')
    num = models.PositiveIntegerField()
    name = models.CharField(primary_key=True, max_length=200)
    amount = models.IntegerField()

    price = models.PositiveIntegerField('권장판매가')
    sale_price = models.PositiveIntegerField('실제판매가')

    is_deleted = models.BooleanField('삭제여부', default=False)
    delete_date = models.DateTimeField('삭제날짜', null=True, blank=True)
    is_hidden = models.BooleanField('노출여부', default=False)
    is_sold_out = models.BooleanField('품절여부', default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    kind = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    img_url = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    questions = GenericRelation(MallsQuestion, related_query_name="question")
    like_item = models.ManyToManyField('MallsList', related_name='like_items')


    def colors(self):
        colors = []
        product_reals = self.product_reals.all()
        for product_real in product_reals:
            colors.append(product_real.option_2_name)

        html = ''

        for color in set(colors):
            if color == '베이지':
                rgb_color = '#f5f5dc'
            elif color == '블랙':
                rgb_color = 'black'
            elif color == '네이비':
                rgb_color = '#000080'
            elif color == '보라':
                rgb_color = '#8b00ff'
            elif color == '민트':
                rgb_color = '#32b489'
            html += f"""<span style="width:10px; height:10px; display:inline-block; border-radius:50%; margin:0 3px; background-color:{rgb_color};"></span>"""

        return html



class ProductReal(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    product = models.ForeignKey(MallsItem, on_delete=models.CASCADE, related_name="product_reals")
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
    is_hidden = models.BooleanField('노출여부', default=False)
    add_price = models.IntegerField('추가가격', default=0)
    stock_quantity = models.PositiveIntegerField('재고개수', default=0)  # 품절일때 유용함



class Post(models.Model):
    like = GenericRelation('Like', related_query_name='post')

class Comment(models.Model):
    like = GenericRelation('Like', related_query_name='comment')
    
    
class Like(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() 
    content_object = GenericForeignKey('content_type', 'object_id')
    # contenttypes과는 무관한 user
    user = models.ForeignKey('accounts.User',
                             on_delete=models.CASCADE)