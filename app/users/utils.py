from app import db

def is_authorized(username: str) -> bool:
    user = db.find_user(username)
    return user is not None