from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
# Create your models here.




class User(AbstractUser):
  class GenderChoices(models.TextChoices) :
    MALE = "M", "남성"
    FEMALE = "F", "여성"
    
  first_name = None
  last_name = None
  
  name = models.CharField('이름', max_length=100)
  profile_img = models.ImageField('프로필이미지', blank=True, choices=GenderChoices.choices, upload_to = "accounts/profile_img/%Y/%m/%d",
                                  help_text='gif/png/jpg 이미지를 업로드 해주세요.')
  
  
  
  
  