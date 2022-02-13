from .common import *

DEBUG = False

KAKAO_KEY = os.environ.get("KAKAO_KEY")
kakao_redirect_uri = os.environ.get("KAKAO_REDIRECT_URI")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mutbly_prod',
        'USER': 'sbsstlocal',
        'PASSWORD': '1234',
        'HOST': '172.17.0.1',
        'PORT': 3306,
    }
}