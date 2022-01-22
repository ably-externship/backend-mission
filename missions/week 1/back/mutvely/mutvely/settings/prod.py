import pymysql  
from .common import *

DEBUG = False 

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mutvely',
        'USER': 'admin',
        'PASSWORD': 'dlatpdk526',
        'HOST':'seahdb.cdy6qymkgosc.ap-northeast-2.rds.amazonaws.com',
        'PORT':'3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
