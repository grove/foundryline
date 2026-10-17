"""Synthetic example only. Do not execute as part of a Gapline audit."""


def register(username: str) -> dict[str, str]:
    """Return an in-memory registration record in this teaching fixture."""
    if not username:
        raise ValueError("username required")
    return {"username": username}
