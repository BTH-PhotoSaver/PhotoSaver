#!/usr/bin/python3

import os

from bucket import Bucket
from datetime import datetime
from exceptions import UnsupportedFileTypeError, FileUnspecifiedError, ImageTitleMissingError
from constants import SUPPORTED_FILE_TYPES


class ImageStore:
    def __init__(self, local_store_path: str, online_store: Bucket, database):
        self.online_store = online_store
        self.local_store_path = local_store_path
        self.database = database
        self.__init_local_store()

    def __init_local_store(self):
        if not os.path.exists(self.local_store_path):
            os.makedirs(self.local_store_path)

    def save(self, file, title, description):
        timestamp_utc = datetime.utcnow()

        if not title:
            raise ImageTitleMissingError()
        if not file:
            raise FileUnspecifiedError()

        filename = self.__get_file_name(file, timestamp_utc)
        filetype = filename.split('.')[1]

        if filetype not in SUPPORTED_FILE_TYPES:
            raise UnsupportedFileTypeError()

        filepath = self.__get_file_path(filename)

        self.__write_to_local_store(file, filepath)
        self.__write_to_online_store(filename, filepath)
        self.__write_to_database(filename, title, description, timestamp_utc)
        self.__remove_from_local_store(filepath)

    def fetch_all(self):
        image_items = []
        self.database.cursor.execute(f'SELECT * FROM {self.database.image_table_name} ORDER BY uploaded')
        for row in self.database.cursor.fetchall():
            id = row[0]
            imagepath = row[1]
            title = row[2]
            description = row[3]
            uploaded = str(row[4]).split(' ')[0]
            image_items.append(
                {'id': id, 'imagepath': imagepath, 'title': title, 'description': description, 'uploaded': uploaded})
        return image_items

    def __write_to_online_store(self, filename, filepath):
        data = open(filepath, 'rb')
        self.online_store.add(Key=f'{self.online_store.image_folder_path}{filename}', Body=data)

    def __write_to_database(self, filename, title, description, uploaded):
        imagepath = f'{self.online_store.image_folder_path}{filename}'
        sql = f'''
    INSERT INTO {self.database.image_table_name} (imagepath, title, description, uploaded) VALUES (%s, %s, %s, %s)
    '''
        self.database.cursor.execute(sql, (imagepath, title, description, uploaded))
        self.database.commit()

    def __write_to_local_store(self, file, filepath):
        with open(filepath, 'wb') as destination:
            destination.write(file.file.read())

    def __remove_from_local_store(self, filepath):
        os.remove(filepath)

    def __get_file_path(self, filename):
        write_file_path = f'{self.local_store_path}{filename}'
        return write_file_path

    def __get_file_name(self, file, timestamp_utc):
        timestamp_str = self.__get_current_timestamp_str(timestamp_utc)
        filename = file.filename.split('.')[0]
        type = file.filename.split('.')[1]
        return f'{filename}_{timestamp_str}.{type}'

    def __get_current_timestamp_str(self, timestamp_utc):
        timestamp = str(timestamp_utc)
        timestamp = timestamp.split('.')[0]
        timestamp = timestamp.replace(':', '').replace('-', '').replace(' ', '-')
        return timestamp
