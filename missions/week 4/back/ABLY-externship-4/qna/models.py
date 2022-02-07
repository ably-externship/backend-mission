from django.db import models
from core.models import TimeStampedModel
from accounts.models import Customer
from products.models import BaseMerchandise

# Create your models here.


class Question(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name='유저')
    basemerchandise = models.ForeignKey(BaseMerchandise, on_delete=models.SET_NULL, null=True, verbose_name='상품')
    title = models.CharField(max_length=20, verbose_name='상품문의 제목')
    content = models.CharField(max_length=255, verbose_name='상품문의 내용')
    
    class Meta:
        verbose_name_plural = '1. 상품문의 목록'
        db_table = 'questions'
    
    def __str__(self):
        return str(self.id)


class Answer(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, verbose_name='상품문의')
    basemerchandise = models.ForeignKey(BaseMerchandise, on_delete=models.SET_NULL, null=True, verbose_name='상품')
    content = models.CharField(max_length=255, verbose_name='상품답변 내용')
    
    class Meta:
        verbose_name_plural = '2. 상품답변 목록'
        db_table = 'answers'
    
    def __str__(self):
        return str(self.id)