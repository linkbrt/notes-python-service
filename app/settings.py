import os

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

POSTGRES_CONFIG = {
    "dbname": os.environ.get('POSTGRES_DBNAME'),
    "user": os.environ.get('POSTGRES_USER'),
    "password": os.environ.get('POSTGRES_PASSWORD'),
    "host": os.environ.get('POSTGRES_HOST'),
}

YANDEX_SPELLER_API_HOST = 'https://speller.yandex.net/services/spellservice.json/checkText'
