from aiohttp import web

from . import views


def get_routes() -> list[web.RouteDef]:
    return [
        web.get('/', views.get_notes),
        web.post('/create-note', views.create_note),
    ]
