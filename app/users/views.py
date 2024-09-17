from aiohttp import web
import psycopg2


USERS = {
    'user1': 'pass1',
    'user2': 'pass2'
}

def registration():
    pass


def authenticate(header_value):
    return header_value in USERS

def authorized(user, password):
    user = USERS.get(user)
    if not user:
        return False

    return user == password


print(authorized('fdag', None))