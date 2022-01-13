#!/usr/bin/python3

from boto3 import session
import json


class Secret:
    def __init__(self, secret_id, region='us-east-1'):
        self.secret_id = secret_id
        self.region = region
        self.session = session.Session()
        self.secretsmanager = self.__get_secretsmanager()
        self.secret = self.__get_secret_json().get('SecretString')

    def get(self, key):
        return json.loads(self.secret)[key]

    def __get_secretsmanager(self):
        return self.session.client(service_name='secretsmanager', region_name=self.region)

    def __get_secret_json(self):
        return self.secretsmanager.get_secret_value(SecretId='icc_database_secret')
