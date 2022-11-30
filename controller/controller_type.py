from typing import TypedDict


class Response(TypedDict):
    data: int | str | None
    ok: str
    message: str
