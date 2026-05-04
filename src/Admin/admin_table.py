from dataclasses import dataclass


@dataclass
class AdminTable:
    num: int
    username: str
    role: str
