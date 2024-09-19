from aiohttp import web

from app import db
from app import utils as app_utils
from app.users.models import User


def is_authorized(request: web.Request) -> User:
    token = request.headers.get('Authorization')
    if token is None:
        raise web.HTTPUnauthorized

    decoded = app_utils.decode_token(token.split(' ')[-1])

    if not decoded:
        raise web.HTTPUnauthorized

    if decoded == "Expired Signature!":
        raise web.HTTPUnauthorized(text=decoded)

    user = db.find_user(decoded)

    if not user:
        raise web.HTTPUnauthorized

    return user


def refresh_tokens(old_access_token: str, refresh_token: str) -> str:
    decoded = app_utils.decode_token(old_access_token, False)
    print(decoded)
    if not decoded:
        raise web.HTTPUnauthorized

    user = db.find_user(decoded)
    print(user)
    if not user or user.refresh_token != refresh_token:
        raise web.HTTPUnauthorized

    return app_utils.create_access_token(user.username)
