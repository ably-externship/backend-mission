import jwt

from django.http import JsonResponse

from accounts.models import User
from my_settings import SECRET_KEY, ALGORITHM

def login_required(func):
    def wrapper(self, request, *arg, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            if not access_token:
                return JsonResponse({'message' : 'Unauthorized Access'}, status=401)

            payload = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user = User.objects.get(id = payload['id'])

            if user.userinfo.is_deleted:
                return JsonResponse({'message' : 'Invalid User'}, status = 401)
            
            request.user = user
            
        except jwt.DecodeError:
            JsonResponse({'message' : 'Unauthorized Token'}, status = 401)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'Invalid User'}, status = 401)
        
        return func(self, request, *arg, **kwargs)
    return wrapper