from dataclasses import dataclass


@dataclass
class OrderTable:
    num: int
    customer_id: int | None = None
    drink: str = ""
    price: str = ""
    quantity: int = 0
    total_price: str = ""
