from .common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ably',
        'USER':'kjkim',
        'PASSWORD':'kj123!@#',
        'HOST':'ec2-18-216-117-18.us-east-2.compute.amazonaws.com',
        'PORT':'3306',
        'OPTIONS': {
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ALLOWED_HOSTS = ['ec2-18-216-117-18.us-east-2.compute.amazonaws.com', '127.0.0.1', 'localhost', 'www.kj-dev.com']

KAKAO_REDIRECT_URI= 'http://127.0.0.1:8000/auth/kakao/login/callback/'