from dataclasses import dataclass


@dataclass
class Table:
    num: int
    drink_name: str
    coffee_type: str
    price: str
    quantity: int
    total_price: str
