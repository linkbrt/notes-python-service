from aiohttp import web

from .. import db
from . import utils as user_utils


async def registration(request: web.Request) -> web.Response:
    data = await request.post()
    username, password = data.get('username'), data.get('password')

    if not username or not password:
        raise web.HTTPBadRequest()

    if db.find_user(username):
        raise web.HTTPBadRequest()

    access_token, refresh_token = db.register_user(username, password)

    return web.json_response({
        'access_token': access_token,
        'refresh_token': refresh_token
    })


async def refresh_access_token(request: web.Request) -> web.Response:
    token = request.headers.get('Authorization')
    if token is None:
        raise web.HTTPUnauthorized

    data = await request.post()

    access_token = user_utils.refresh_tokens(token.split()[-1],
                                             data.get('refresh_token'))

    return web.json_response({'access_token': access_token})
