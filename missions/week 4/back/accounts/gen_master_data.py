from django.conf import settings
from django.contrib.auth.models import User



def gen_master(apps, schema_deitor) :
  if not settings.DEBUG:
    return
  else :
    User.objects.create_superuser(username='admin', password='12', name = "관리자", email="")
    
    for id in range(2,6):
      username = f"user{id}"
      password = "12"
      name = f"{id}"
      email = f"test{id}@test.com"
      
      User.objects.create_user(username=username, password=password, name = name, email=email)
      
      
      