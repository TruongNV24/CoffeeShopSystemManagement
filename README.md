## Coffee Shop System Management

Dự án gốc dùng JavaFX. Mình đã bổ sung thêm phiên bản **Python + SQLite** để chạy nhanh trong **Visual Studio Code**.

## Python version (VS Code friendly)

Thư mục mới: `python_app/`

### 1) Tạo môi trường

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Khởi tạo database SQLite

```bash
python python_app/app.py init-db
```

File database sẽ được tạo tại:

- `python_app/coffeeshop.db`

### 3) Chạy các lệnh quản lý

```bash
python python_app/app.py list-drinks
python python_app/app.py add-drink Espresso 2.2
python python_app/app.py create-order cashier1 1 2
python python_app/app.py revenue
```

## VS Code config đã thêm

- `.vscode/settings.json`: cấu hình Python interpreter + analysis.
- `.vscode/launch.json`: cấu hình debug nhanh cho CLI Python.

## Ghi chú

- Database dùng **SQLite** như yêu cầu.
- Schema gồm: `users`, `drinks`, `orders`, `order_items`.
