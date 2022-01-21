import json
import jwt
import bcrypt

from django.http import JsonResponse
from django.views import View

from accounts.models import Account
from core.const import USER_ACCOUNT_TYPE
from my_settings import SECRET_KEY, ALGORITHM

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            password = data['password']
            
            account = Account.objects.get(
                email = data['email'], 
                account_type_id = USER_ACCOUNT_TYPE,
                user__social_type_id__isnull = True,
                is_deleted = False)

            if not bcrypt.checkpw(password.encode('utf-8'), account.password.encode('utf-8')):
                return JsonResponse({'message' : 'Invalid User'}, status = 401)

            access_token = jwt.encode({'id' : account.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({
                'access_token' : access_token, 
                'account_type' : account.account_type.account_type
                }, status = 201)
        
        except KeyError:
            return JsonResponse({'message' : 'Key Error'}, status = 400)
        except Account.DoesNotExist:
            return JsonResponse({'message' : 'Invalid User'}, status = 401)