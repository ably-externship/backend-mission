from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class UserManager(UserManager):
    pass

class MallsItems(models.Model):
    id = models.ForeignKey('MallsList', models.DO_NOTHING, db_column='id')
    num = models.PositiveIntegerField()
    name = models.CharField(primary_key=True, max_length=200)
    amount = models.IntegerField()
    price = models.PositiveIntegerField()
    # default 'y' 판매 : 'y', 판매중단 : 'n'
    useyn = models.CharField(max_length=50)
    #  	top : 1, bottom : 2, dress : 3, bag : 4, shoes : 5, acc : 6
    kind = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image_url = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    regdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'malls_items'


class MallsList(models.Model):
    shop = models.CharField(max_length=80)
    kind = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'malls_list'


class MallsQuestion(models.Model):
    q_num = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    reply = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    rep = models.CharField(max_length=1)
    date = models.DateField()

    class Meta:
        managed = True
        db_table = 'malls_question'
