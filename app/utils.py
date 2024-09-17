import jwt

import settings
from datetime import datetime as dt


def create_tokens(user_id):
    current_datetime = dt.now()

    access_token =  jwt.encode(
        payload + {"token_type": "access"}, 
        key=settings.JWT_SECRET_KEY, 
        algorithm="HS256"
    )

    refresh_token = jwt.encode(
        payload + 
    )