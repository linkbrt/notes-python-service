from typing import Union
import jwt
from cryptography.fernet import Fernet
from . import settings
from datetime import datetime, timedelta


def create_tokens(username) -> Union[str, str]:
    current_datetime = datetime.now()

    payload = {
        "username": username,
        "token_type": "access",
        "exp": current_datetime + timedelta(minutes=3)
    }

    access_token =  jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY, 
        algorithm="HS256",
    )

    refresh_token = str(Fernet.generate_key())[2:-1]
    
    return access_token, refresh_token


def decode_token(token: str) -> str:
    print(token.split())
    try:
        return jwt.decode(token.split()[1], key=settings.JWT_SECRET_KEY, algorithms="HS256").get('username')
    except Exception as e:
        print(e)
        return "Error"
