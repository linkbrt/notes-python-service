import psycopg2

from settings import POSTGRES_CONFIG

def get_connection():
    return psycopg2.connect(' '.join([f"{key}={value}" for key, value in POSTGRES_CONFIG.items()]))


def get_users():
    