#!/usr/bin/python3

from psycopg2 import connect
from constants import IMAGE_TABLE_NAME


class Database:
    def __init__(self, host, database, user, password, image_table_name=IMAGE_TABLE_NAME):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.image_table_name = image_table_name
        self.__db = connect(host=host, database=database, user=user, password=password)
        self.cursor = self.__db.cursor()

    def commit(self):
        self.__db.commit()
