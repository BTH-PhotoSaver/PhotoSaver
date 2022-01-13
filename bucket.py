#!/usr/bin/python3

from boto3 import resource
from constants import BUCKET_IMAGE_FOLDER_PATH

S3 = 's3'


class Bucket:
    def __init__(self, name, image_folder_path=BUCKET_IMAGE_FOLDER_PATH, region='us-east-1'):
        self.name = name
        self.image_folder_path = image_folder_path
        self.region = region
        self.s3_service = resource(S3, region_name=region)
        self.__bucket = self.s3_service.Bucket(name)

    def add(self, *args, **kwargs):
        self.__bucket.put_object(*args, **kwargs)


