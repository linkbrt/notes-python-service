from aiohttp import web

from . import views


def get_routes() -> list[web.RouteDef]:
    return [
        web.post('/register', views.registration),
        web.post('/refresh-token', views.refresh_access_token),
    ]
