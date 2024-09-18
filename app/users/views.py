from aiohttp import web
import psycopg2

from .. import db


async def registration(request: web.Request) -> web.Response:
    # return web.json_response(db.get_users())
    data = await request.post()
    username, password = data.get('username'), data.get('password')
    
    if not username or not password:
        raise web.HTTPBadRequest()
    
    if db.find_user(username):
        raise web.HTTPBadRequest()
    
    access_token, refresh_token = db.register_user(username, password)
    
    return web.json_response({'access_token': access_token, 'refresh_token': refresh_token})


# def authenticate(header_value):
#     return header_value in USERS

# def authorized(user, password):
#     user = USERS.get(user)
#     if not user:
#         return False

#     return user == password


# print(authorized('fdag', None))