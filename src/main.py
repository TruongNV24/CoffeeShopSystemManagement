from Admin.admin import offline_status, get_current_admin
from db import connect


def query_check_cancel_pending() -> None:
    admin = get_current_admin()
    if not admin:
        return
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT COUNT(1) FROM history WHERE status='Accepted' AND accepted_by=%s", (admin,))
        if cur.fetchone()[0]:
            cur.execute("UPDATE history SET status='Pending', accepted_by=NULL WHERE status='Accepted' AND accepted_by=%s", (admin,))
            conn.commit()


def main() -> None:
    try:
        print('Coffee Shop System Management (Python backend migration)')
    finally:
        offline_status()
        query_check_cancel_pending()


if __name__ == '__main__':
    main()
