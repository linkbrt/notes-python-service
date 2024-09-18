from typing import List
import psycopg2

from .users.models import User

from .utils import create_tokens
from .settings import POSTGRES_CONFIG

def get_connection():
    # print(' '.join([f"{key}={value}" for key, value in POSTGRES_CONFIG.items()]))
    return psycopg2.connect(' '.join([f"{key}={value}" for key, value in POSTGRES_CONFIG.items()]))


def get_users() -> List[User]:
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [User(*user) for user in users]

def find_user(username: str) -> User | None:
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))

    user = cur.fetchone()
    return User(*user) if user else None

def register_user(username: str, password: str):
    conn = get_connection()
    cur = conn.cursor()
    
    access_token, refresh_token = create_tokens(username)
    
    cur.execute("INSERT INTO users (username, password, refresh_token) VALUES (%s, %s, %s)", 
                (username, password, refresh_token))
    
    conn.commit()
    
    cur.close()
    conn.close()

    return access_token, refresh_token