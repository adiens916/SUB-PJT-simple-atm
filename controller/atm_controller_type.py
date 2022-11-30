from typing import TypedDict


class Response(TypedDict):
    data: int | None
    ok: str
    message: str
