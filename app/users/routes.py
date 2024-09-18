from aiohttp import web

from . import views

def get_routes():
    return [
        web.post('/register', views.registration),
    ]