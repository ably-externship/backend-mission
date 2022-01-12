from django.db import models
from user.models import User

# Order table
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now=True,verbose_name='주문시간')
    status = models.CharField(max_length=128, verbose_name='주문상태')

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users') # related_name으로 역참조 가능

    def __str__(self):
        return self.datetime