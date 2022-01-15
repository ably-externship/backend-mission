from os import access
import jwt

from django.http  import JsonResponse
from django.views import View
from django.db import transaction

from accounts.models     import User, SocialType, SocialUserInfo
from core.utils import KakaoAPI
from my_settings import SECRET_KEY, ALGORITHM

class KakaoLoginView(View):
    def get(self, request):
        
        token = request.headers['Authorization']
        
        kakao_client = KakaoAPI(token)
        user_info = kakao_client.get_user()
        email = user_info['kakao_account']['email']

        with transaction.atomic():
            user, created = User.objects.get_or_create(email = email)
            social_type = SocialType.objects.get(social_type='kakao')
            social_user, created = SocialUserInfo.objects.get_or_create(user_id = user.id, social_type_id = social_type.id)

        access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

        return JsonResponse({'access_token' : access_token}, status=200)