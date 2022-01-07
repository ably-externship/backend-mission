from django.db import models


# # Create your models here.
# #상품질문

class Question(models.Model):
    shop = models.ForeignKey('mall.Shop', on_delete=models.CASCADE, verbose_name='쇼핑몰')
    #product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    # user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')

    category = models.CharField(choices=(
        ('상품질문', 'product'),
        ('배송관련', 'delivery')
    ), default="productQuestion", max_length=32, verbose_name='질문 카테고리')

    title = models.CharField(max_length=256, verbose_name='질문제목')
    description = models.TextField(verbose_name='상품질문')


class Answer(models.Model):
    # 답변
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='질문')
    answer = models.TextField(verbose_name='답변')
