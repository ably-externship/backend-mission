import json
import jwt
import bcrypt

from django.http import JsonResponse
from django.views import View

from accounts.models import User
from my_settings import SECRET_KEY, ALGORITHM

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            password = data['password']
            user = User.objects.get(email = data['email'], is_social = False)

            if user.userinfo.is_deleted:
                return JsonResponse({'message' : 'Invalid User'}, status = 401)

            if not bcrypt.checkpw(password.encode('utf-8'), user.userinfo.password.encode('utf-8')):
                return JsonResponse({'message' : 'Invalid User'}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'access_token' : access_token}, status = 201)
        
        except KeyError:
            return JsonResponse({'message' : 'Key Error'}, status = 400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'Invalid User'}, status = 401)