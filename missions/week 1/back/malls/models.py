from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.utils import timezone 
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
        db_table = 'malls_items'


class MallsList(models.Model):
    shop = models.CharField(max_length=80)
    kind = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    class Meta:
        db_table = 'malls_list'


class MallsQuestion(models.Model):
    q_num = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    reply = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('MallsUser', models.DO_NOTHING, blank=True, null=True)
    rep = models.CharField(max_length=1)
    date = models.DateField()

    class Meta:
        db_table = 'malls_question'

# class Post(models.Model): # Post 모델의 이름, models는 Post가 장고 모델임을 의미
#     author = models.ForeignKey('malls.User', models.DO_NOTHING) # 작성자명
#     title = models.CharField(max_length=200) # 제목, 길이제한 O
#     text = models.TextField() # 내용, 길이제한 X
#     created_date = models.DateTimeField(default=timezone.now) # 최초생성시각
#     published_date = models.DateTimeField(blank=True, null=True) # 발행날짜

#     def publish(self): # 발행
#         self.published_date = timezone.now() # 현재시각 저장
#         self.save()

#     def __str__(self): # _ _ 2개
#         return self.title


class MallsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'malls_user'


