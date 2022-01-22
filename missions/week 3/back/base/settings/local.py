from .common import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '127.0.0.1:3000', 'localhost:3000']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ably',
        'USER': 'kjkim',
        'PASSWORD': 'kj123!@#',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CORS_ALLOWED_ORIGINS = [
	# 허용할 Origin 추가
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
CORS_ALLOW_CREDENTIALS = True
APPEND_SLASH = False
