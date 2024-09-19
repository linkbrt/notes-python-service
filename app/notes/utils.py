import aiohttp

from .. import db, settings

from .models import Note, YandexWordError


async def save_note(text: str, user_id: int) -> bool:
    note = Note(1, text=text, user_id=user_id)

    note.text = await check_note_in_yandex_api(note)

    return db.save_note(note)


async def check_note_in_yandex_api(note: Note) -> str:
    params = {'text': note.text}

    async with aiohttp.ClientSession() as session:
        async with session.get(settings.YANDEX_SPELLER_API_HOST,
                               params=params) as resp:
            text = await resp.json()
            new_text = change_errors(
                note.text, [YandexWordError(**item) for item in text])

    return new_text


def change_errors(text: str, errors: list[YandexWordError]) -> str:
    i = 0
    result = []

    for error in errors:
        while i < len(text):
            if i == error.pos:
                result.append(error.s[0])
                i += error.len
                break
            else:
                result.append(text[i])
                i += 1

    return ''.join(result)
