from datetime import datetime, timedelta
from typing import Union

import jwt
from cryptography.fernet import Fernet

from app import settings


def create_tokens(username) -> Union[str, str]:
    access_token = create_access_token(username)
    refresh_token = str(Fernet.generate_key())[2:-1]
    return access_token, refresh_token


def create_access_token(username):
    current_datetime = datetime.now()

    payload = {
        "username": username,
        "token_type": "access",
        "exp": (current_datetime + timedelta(hours=1)).timestamp()
    }

    access_token = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm="HS256",
    )

    return access_token


def decode_token(token: str, verify_signature: bool = True) -> str:
    try:
        return jwt.decode(token,
                          key=settings.JWT_SECRET_KEY,
                          algorithms="HS256",
                          options={
                              "verify_signature": verify_signature
                          }).get('username')
    except jwt.DecodeError:
        return ""
    except jwt.ExpiredSignatureError:
        return "Expired Signature!"
    except Exception as e:
        print(e)
        print("Cannot decode for unusual reason")
