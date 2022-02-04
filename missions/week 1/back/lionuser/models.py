from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser

from django.contrib.auth import get_user_model
class LionuserManager(UserManager):
    use_in_migrations = True
#     #
    # def _create_user(self, username, email, password, **extra_fields):
    #     """
    #     Create and save a user with the given username, email, and password.
    #     """
    #     if not username:
    #         raise ValueError('The given username must be set')
    #     email = self.normalize_email(email)
    #     # Lookup the real model class from the global app registry so this
    #     # manager method can be used in migrations. This is fine because
    #     # managers are by definition working on the real model.
    #     GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
    #     username = GlobalUserModel.normalize_username(username)
    #     user = self.model(username=username, email=email, **extra_fields)
    #     user.password = make_password(password)
    #     user.save(using=self._db)
    #     return user

#custome AuthUser https://www.youtube.com/watch?v=AfYfvjP1hK8&t=4345s
class Lionuser(AbstractUser): #AbstractBaseUser,PermissionsMixin
    """
    customized User
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    email = models.EmailField(
        max_length=64,
        unique=True,
        help_text='EMAIL ID.'
    )
    username = models.CharField(
        max_length=30,
        unique=True
    )
    password = models.TextField() # password 컬럼 상속?
    #phone_number = models.TextField()
    #objects = LionuserManager()

    USERNAME_FIELD = 'username'

    class UserTypeCodeChoices(models.TextChoices):
        ADMIN = "ABLY 최고 관리자"
        M_ADMIN = "마켓관리자"
        USER = "사용자"
    #
    user_type = models.CharField('유저타입', max_length=20, choices=UserTypeCodeChoices.choices,
                                          default=UserTypeCodeChoices.M_ADMIN)
        # models.CharField(choices=(
        # ('ADMIN', 'ABLY 최고 관리자'),
        # ('M_ADMIN', '마켓관리자'),
        # ('USER', '사용자')
        # ),  default="M_ADMIN", max_length=32, verbose_name='유저타입')

    #테이블 추가 OR 컬럼 추가 선택
    shop = models.ForeignKey('mall.Shop', on_delete=models.CASCADE, verbose_name='쇼핑몰', default = 1) #1:N


    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    # #
    # # def __str__(self):
    # #     return self.username
    #
    # def get_short_name(self):
    #     return self.email
