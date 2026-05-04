from dataclasses import dataclass


@dataclass
class DrinkTable:
    num: int
    drink_name: str
    hot_price: str
    iced_price: str
    frappee_price: str
