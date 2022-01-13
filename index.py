#!/usr/bin/python3
import requests

from bottle import route, run
from secret import Secret
from database import Database
from bucket import Bucket
from imagestore import ImageStore
from constants import LOCAL_IMAGE_FOLDER_PATH, BUCKET_TITLE
from homepage import Homepage
from uploadpage import UploadPage

@route('/')
def get_homepage():
    return Homepage(image_store).render()


@route('/upload', method='GET')
def get_upload_page():
    return UploadPage().render_get()


@route('/upload', method='POST')
def post_image():
    return UploadPage().render_post(image_store)


if __name__ == '__main__':
    print("STARTING SERVER...")
    print("FETCHING SECRETS...")
    secret = Secret('icc_database_secret')

    username = secret.get('username')
    host = secret.get('host')
    password = secret.get('password')
    dbname = secret.get('dbname')

    print("INSTANTIATING TO DB...")
    db = Database(host, dbname, username, password)
    cursor = db.cursor

    print("SETTING SCHEMA...")
    cursor.execute("SET SCHEMA 'image_data';")
    db.commit()

    print("INSTANTIATING BUCKET...")
    bucket = Bucket(BUCKET_TITLE)

    print("CREATING IMAGESTORE...")
    image_store = ImageStore(LOCAL_IMAGE_FOLDER_PATH, bucket, db)

    # fetch public IPv4 DNS
    instance_url = requests.get('http://169.254.169.254/latest/meta-data/public-hostname').text

    # make the website available under port 80
    run(host=instance_url, port=80)
