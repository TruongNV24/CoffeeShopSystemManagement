from typing import Protocol
from .coffee import Coffee


class MyListener(Protocol):
    def on_click_listener(self, coffee: Coffee) -> None: ...
