from typing import TypedDict


class Response(TypedDict):
    data: int | str
    ok: str
    message: str
