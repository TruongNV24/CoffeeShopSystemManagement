from dataclasses import dataclass


@dataclass
class Coffee:
    name: str
    hot_price: float
    iced_price: float
    frappee_price: float
    img_src: str

    CURRENCY = "$"
