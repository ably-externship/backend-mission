from django.db import models

from core.models import TimeStampModel
from accounts.models import User, Seller
from products.models import Product

class QuestionCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'question_categories'

class Question(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    answered = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'questions'

class Answer(TimeStampModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'answers'