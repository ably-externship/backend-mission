from os import access
from django.http import JsonResponse
import requests

class KakaoAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_user(self):
        self.url = 'https://kapi.kakao.com/v2/user/me'
        self.headers = {'Authorization' : f"Bearer {self.access_token}"}

        response = requests.get(self.url, headers=self.headers).json()

        return response