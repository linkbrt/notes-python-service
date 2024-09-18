from aiohttp import web

from app.notes import views

def get_routes():
    return [
        web.get('/', views.get_notes),
    ]