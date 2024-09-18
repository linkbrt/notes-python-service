from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    password: str
    refresh_token: str = ""
