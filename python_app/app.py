from __future__ import annotations

import argparse

from database import get_connection, init_db, seed_data


def list_drinks() -> None:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, name, price FROM drinks ORDER BY id").fetchall()
    if not rows:
        print("No drinks found.")
        return
    for row in rows:
        print(f"{row['id']:>2}. {row['name']:<12} ${row['price']:.2f}")


def add_drink(name: str, price: float) -> None:
    with get_connection() as conn:
        conn.execute("INSERT INTO drinks(name, price) VALUES (?, ?)", (name, price))
        conn.commit()
    print(f"Added drink: {name} (${price:.2f})")


def create_order(username: str, drink_id: int, quantity: int) -> None:
    with get_connection() as conn:
        user = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if user is None:
            conn.execute("INSERT INTO users(username, role) VALUES (?, 'cashier')", (username,))
            user = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()

        drink = conn.execute("SELECT price FROM drinks WHERE id = ?", (drink_id,)).fetchone()
        if drink is None:
            raise ValueError("Drink not found")

        cursor = conn.execute("INSERT INTO orders(user_id, status) VALUES (?, 'pending')", (user["id"],))
        order_id = cursor.lastrowid
        conn.execute(
            "INSERT INTO order_items(order_id, drink_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
            (order_id, drink_id, quantity, drink["price"]),
        )
        conn.commit()
    print(f"Created order #{order_id} for {username}")


def revenue_report() -> None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total
            FROM orders o
            JOIN order_items oi ON oi.order_id = o.id
            WHERE o.status IN ('confirmed', 'completed')
            """
        ).fetchone()
    print(f"Revenue (confirmed + completed): ${row['total']:.2f}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Coffee Shop Management (Python + SQLite)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init-db", help="Create SQLite database and seed data")
    sub.add_parser("list-drinks", help="List all drinks")

    add_parser = sub.add_parser("add-drink", help="Add a new drink")
    add_parser.add_argument("name")
    add_parser.add_argument("price", type=float)

    order_parser = sub.add_parser("create-order", help="Create an order")
    order_parser.add_argument("username")
    order_parser.add_argument("drink_id", type=int)
    order_parser.add_argument("quantity", type=int)

    sub.add_parser("revenue", help="Show revenue report")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init-db":
        init_db()
        seed_data()
        print("Database initialized.")
    elif args.command == "list-drinks":
        list_drinks()
    elif args.command == "add-drink":
        add_drink(args.name, args.price)
    elif args.command == "create-order":
        create_order(args.username, args.drink_id, args.quantity)
    elif args.command == "revenue":
        revenue_report()


if __name__ == "__main__":
    main()
