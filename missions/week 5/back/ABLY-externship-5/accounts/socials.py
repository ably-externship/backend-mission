from django.views import View
from collections import defaultdict
import requests
import os

class SocialLoginProfile(View):
    
    def kakao(request, access_code):
        
        client_id = os.environ.get('KAKAO_CLIENT_ID')
        redirect_uri = 'http://127.0.0.1:8000/accounts/login/social/kakao'
        code = access_code
        
        api_url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}'
        token_response = requests.get(api_url)
        if token_response.status_code != 200:
            return token_response
        token_json = token_response.json()
        access_token = token_json['access_token']
        
        
        profile_url = 'https://kapi.kakao.com/v2/user/me'
        headers = {'Authorization' : f'Bearer {access_token}'}
        profile_response = requests.get(profile_url, headers=headers)
        if profile_response.status_code != 200:
            return profile_response
        profile_json = profile_response.json()
        
        data = defaultdict(str)
        data['social_id'] = str(profile_json['id'])
        data['name'] = str(profile_json['properties']['nickname'])
        data['phone_number'] = str(os.environ.get('PHONE_NUMBER'))
        if 'email' in list(profile_json['kakao_account'].keys()):
            data['email'] = str(profile_json['kakao_account']['email'])
        if 'phone' in list(profile_json['kakao_account'].keys()):
            data['phone_number'] = str(profile_json['kakao_account']['phone'])
        if 'birthday' in list(profile_json['kakao_account'].keys()):
            data['birthday'] = str(profile_json['kakao_account']['birthday'])
        if 'birthyear' in list(profile_json['kakao_account'].keys()):
            data['birthyear'] = str(profile_json['kakao_account']['birthyear'])
        
        return data
    
    def naver(request, access_code):
        pass