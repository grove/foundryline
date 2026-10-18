"""Authored example candidate — not the output of a recorded coding agent.

The original illustrative request lives in ../original-request.md.
"""


def register_username(username: str) -> str:
    """Return a valid username unchanged; reject empty/whitespace-only strings."""
    if not username.strip():
        raise ValueError("username cannot be blank")
    return username
