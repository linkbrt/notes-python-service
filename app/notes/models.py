from dataclasses import dataclass


@dataclass
class Note:
    id: int = -1
    text: str = ''
    user_id: int = -1


@dataclass
class YandexWordError:
    code: int
    pos: int
    row: int
    col: int
    len: int
    word: str
    s: list[str]