from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.fields import EmailField

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not password:
            raise ValueError('Password is Required')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        superuser = self.create_user(username=username, password=password, **extra_fields)
        superuser.set_password(password)
        superuser.is_superuser = True
        superuser.is_admin = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model
    """
    objects = UserManager()
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    password = models.CharField(max_length=255, verbose_name='비밀번호')
    email = EmailField(unique=True, blank=True, null=True, verbose_name='이메일')
    is_seller = models.BooleanField(default=False, verbose_name='셀러')
    brand = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='브랜드')
    created = models.DateTimeField(auto_now_add=True, verbose_name='가입 날짜')
    updated = models.DateField(auto_now=True, verbose_name='업데이트 날짜')
    # default
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    is_staff = models.BooleanField(default=False, verbose_name='스태프')
    is_admin = models.BooleanField(default=False, verbose_name='어드민')
    is_superuser = models.BooleanField(default=False, verbose_name='슈퍼유저')
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ''
    
    class Meta:
        verbose_name_plural = '1. 유저 목록'
        db_table = 'users'
    
    def __str__(self):
        return str(self.id)