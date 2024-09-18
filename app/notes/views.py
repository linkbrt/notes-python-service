from aiohttp import web

from app import utils as app_utils
from app.users import utils


async def get_notes(request: web.Request) -> web.Response:
    username = app_utils.decode_token(request.headers.get('Authorization'))
    print(username)
    user = utils.is_authorized(username)
    if user:
        return web.json_response(data={'some': 'data'})
    
    return web.HTTPUnauthorized()



async def create_note(request: web.Request) -> web.Response:
    return