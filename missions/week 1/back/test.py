# Django 로딩
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

# from account.models import User

# print(User.objects.all())
# User.objects.create_user('h45652','h45652@naver.com','1234')
# from django.core.mail import send_mail
#
# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'min949494@gmail.com',# 발신
#     ['h45652@naver.com'],# 수신
#     fail_silently=False,
# )
