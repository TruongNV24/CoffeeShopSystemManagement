_current_admin = None
_current_admin_role = None


def set_current_admin(username: str) -> None:
    global _current_admin
    _current_admin = username


def get_current_admin() -> str | None:
    return _current_admin


def set_current_admin_role(role: str) -> None:
    global _current_admin_role
    _current_admin_role = role


def get_current_admin_role() -> str | None:
    return _current_admin_role


def active_status() -> None:
    pass


def offline_status() -> None:
    pass
