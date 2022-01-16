from django.db import models
from django.db.models.fields import EmailField
from core.models import TimeStampedModel
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

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


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """
    User Model
    """
    objects = UserManager()
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, verbose_name='아이디')
    password = models.CharField(max_length=255, blank=True, null=True, verbose_name='비밀번호')
    email = EmailField(unique=True, blank=True, null=True, verbose_name='이메일')
    
    # default
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    is_staff = models.BooleanField(default=False, verbose_name='스태프')
    is_admin = models.BooleanField(default=False, verbose_name='어드민')
    is_superuser = models.BooleanField(default=False, verbose_name='슈퍼유저')
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ''
    
    class Meta:
        verbose_name_plural = '1. 전체유저 목록'
        db_table = 'users'
    
    def __str__(self):
        return str(self.id)


class Customer(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False, validators=[RegexValidator(r'^\d{3}-?[1-9]\d{3}-?\d{4}$')], verbose_name='휴대폰 번호')
    is_local = models.BooleanField(default=False, verbose_name='로컬계정')
    connect_social = models.BooleanField(default=False, verbose_name='소셜계정')
    social_type = models.CharField(max_length=8, blank=True, null=True, verbose_name='소셜타입')
    social_id = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='소셜계정 고유식별값')
    
    class Meta:
        verbose_name_plural = '2. 커스토머 목록'
        db_table = 'customers'
    
    def __str__(self):
        return str(self.user)


class Seller(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False, validators=[RegexValidator(r'^\d{3}-?[1-9]\d{3}-?\d{4}$')], verbose_name='휴대폰 번호')
    brand =  models.CharField(max_length=255, verbose_name='브랜드')
    
    class Meta:
        verbose_name_plural = '3. 셀러 목록'
        db_table = 'sellers'
    
    def __str__(self):
        return str(self.user)


class PhoneVerification(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False, validators=[RegexValidator(r'^\d{3}-?[1-9]\d{3}-?\d{4}$')], verbose_name='휴대폰 번호')
    verification_code = models.CharField(max_length=255, verbose_name='인증번호')
    is_verified = models.BooleanField(default=False, verbose_name='인증')
    is_used = models.BooleanField(default=False, verbose_name='가입')
    
    class Meta:
        verbose_name_plural = '4. 휴대폰인증 목록'
        db_table = 'phone_verifications'
    
    def __str__(self):
        return str(self.id)