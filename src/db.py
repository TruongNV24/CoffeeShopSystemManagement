from dataclasses import dataclass
import mysql.connector

@dataclass
class DBConfig:
    host: str = "localhost"
    database: str = "coffeeshop"
    user: str = "coffeeAdmin"
    password: str = "test123"


def connect(config: DBConfig | None = None):
    cfg = config or DBConfig()
    return mysql.connector.connect(
        host=cfg.host,
        database=cfg.database,
        user=cfg.user,
        password=cfg.password,
    )
