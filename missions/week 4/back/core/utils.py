import requests
import uuid

from my_settings import S3_CLIENT, S3_BUCKET_NAME, FOLDER_OBJECT, IMAGE_URL

class KakaoAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_user(self):
        self.url = 'https://kapi.kakao.com/v2/user/me'
        self.headers = {'Authorization' : f"Bearer {self.access_token}"}

        response = requests.get(self.url, headers=self.headers).json()

        return response

def image_uploader(images):
    image_urls = []

    for image in images:
        prefix = str(uuid.uuid4())
        S3_CLIENT.upload_fileobj(
                image, 
                S3_BUCKET_NAME, 
                FOLDER_OBJECT + prefix + image.name,
                ExtraArgs={'ContentType' : image.content_type}
                )
        image_urls.append({'image_url' : IMAGE_URL + prefix + image.name})

    return image_urls
