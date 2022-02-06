from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from .models import Customer, User
import os
import jwt
import datetime


def jwt_publish(user_id):
    jwt_expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*6)
    access_jwt = jwt.encode({'exp': jwt_expiration, 'user_id': user_id}, key=os.environ.get('DJANGO_SECRET_KEY'), algorithm=os.environ.get('ALGORITHM'))
    return access_jwt


def jwt_authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            try:
                access_jwt = request.COOKIES.get('_utk')
            except:
                return JsonResponse({'message': 'GET JWT COOKIE ERROR'}, status=400)
            
            payload = jwt.decode(access_jwt, key=os.environ.get('DJANGO_SECRET_KEY'), algorithms=os.environ.get('ALGORITHM'))
            try:
                user = User.objects.get(id=payload['user_id'])
                request.user = user
            except:
                request.user = payload['user_id']
            return func(self, request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'JWTOKEN EXPIRED'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'INVALID JWTOKEN'}, status=401)
    return wrapper
