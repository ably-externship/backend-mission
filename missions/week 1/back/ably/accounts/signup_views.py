from django.shortcuts import render
import json
import bcrypt

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View
from django.db import transaction

from core.validators import validate_email, validate_password, validate_phone_number, validate_name
from accounts.models import User, UserInfo

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            name = data['name']
            phone_number = data['phone_number']

            validate_email(email)
            validate_password(password)
            validate_name(name)
            validate_phone_number(phone_number)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'Email Already Exists'}, status = 400)

            if UserInfo.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message' : 'Phone Number Already Exists'}, status = 400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            with transaction.atomic():
                user = User(email = email)
                user.save()

                UserInfo.objects.create(
                    user_id = user.id,
                    password = hashed_password,
                    name = name,
                    phone_number = phone_number
                )

            return JsonResponse({'message' : 'Success'}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'Key Error'}, status = 400)
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status = 400)














