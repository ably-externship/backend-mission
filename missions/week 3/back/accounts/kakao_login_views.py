from os import access
import jwt

from django.http  import JsonResponse
from django.views import View
from django.db import transaction

from accounts.models     import Account, User, SocialType, SocialUserInfo
from core.utils import KakaoAPI
from core.const import USER_ACCOUNT_TYPE, KAKAO_SOCIAL_TYPE
from my_settings import SECRET_KEY, ALGORITHM

class KakaoLoginView(View):
    def get(self, request):
        
        token = request.headers['Authorization']
        
        kakao_client = KakaoAPI(token)
        user_info = kakao_client.get_user()
        email = user_info['kakao_account']['email']

        filter_set = {
            'email' : email,
            'is_social' : True,
            'socialuserinfo__social_type_id' : KAKAO_SOCIAL_TYPE
        }

        if User.objects.filter(**filter_set).exists():
            user = User.objects.get(**filter_set)
            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
        
        else:
            with transaction.atomic():
                account = Account(account_type_id = USER_ACCOUNT_TYPE)
                account.save()
                user = User(account_id = account.id, email = email, is_social = True)
                user.save()
                SocialUserInfo.objects.create(user_id = user.id, social_type_id = KAKAO_SOCIAL_TYPE)
            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

        return JsonResponse({'access_token' : access_token}, status=200)