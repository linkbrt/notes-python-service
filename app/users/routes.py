from aiohttp import web

from app.users import views


def get_routes():
    return [
        web.post('/register', views.registration),
        web.post('/refresh-token', views.refresh_access_token),
    ]
