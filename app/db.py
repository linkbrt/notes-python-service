import psycopg2

from app.users.models import User
from app.notes.models import Note

from app.utils import create_tokens
from app.settings import POSTGRES_CONFIG


def get_connection():
    return psycopg2.connect(' '.join(
        [f"{key}={value}" for key, value in POSTGRES_CONFIG.items()]))


""" Users """


def get_users() -> list[User]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return [User(*user) for user in users]


def find_user(username: str) -> User | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=%s", (username, ))

    user = cur.fetchone()
    return User(*user) if user else None


def register_user(username: str, password: str):
    conn = get_connection()
    cur = conn.cursor()

    access_token, refresh_token = create_tokens(username)

    cur.execute(
        "INSERT INTO users (username, password, refresh_token) VALUES (%s, %s, %s)",
        (username, password, refresh_token))

    conn.commit()

    cur.close()
    conn.close()

    return access_token, refresh_token


""" Notes """


def save_note(note: Note) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO notes (text, user_id) VALUES (%s, %s)",
                    (note.text, note.user_id))
        conn.commit()
    except psycopg2.errors.DataException:
        return False

    cur.close()
    conn.close()

    return True


def get_user_notes(user: User) -> list[Note]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, text FROM notes WHERE user_id = %s", (user.id, ))
    data = cur.fetchall()

    cur.close()
    conn.close()

    return [Note(*note) for note in data]
