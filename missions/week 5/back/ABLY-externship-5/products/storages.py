from storages.backends.s3boto3 import S3Boto3Storage
from config.settings.base import AWS_LOCATION

class MediaStorage(S3Boto3Storage):
    location = AWS_LOCATION