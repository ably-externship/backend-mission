from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class LionuserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class Lionuser(AbstractBaseUser,PermissionsMixin):
    """
    customized User
    """
    email = models.EmailField(
        max_length=64,
        unique=True,
        help_text='EMAIL ID.'
    )
    username = models.CharField(
        max_length=30,
    )
    # password = models.TextField(), password 컬럼 상속
    objects = LionuserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    #
    # def __str__(self):
    #     return self.username

    def get_short_name(self):
        return self.email
