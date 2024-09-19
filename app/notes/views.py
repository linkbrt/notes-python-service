from aiohttp import web

from app.users import utils as users_utils
from app.notes import utils as notes_utils

from app import db


async def get_notes(request: web.Request) -> web.Response:
    user = users_utils.is_authorized(request)

    user_notes = db.get_user_notes(user)

    return web.json_response(data=[{
        "id": note.id,
        "text": note.text
    } for note in user_notes])


async def create_note(request: web.Request) -> web.Response:
    user = users_utils.is_authorized(request)

    data = await request.post()
    text = data.get('text')
    if not text:
        raise web.HTTPBadRequest

    if await notes_utils.save_note(text, user.id):
        return web.HTTPCreated()

    return web.HTTPBadRequest
