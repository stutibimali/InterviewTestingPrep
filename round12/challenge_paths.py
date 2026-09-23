from pathlib import PurePosixPath


def safe_filename(name: str) -> str:
    """Return only the final filename component from a user-supplied path."""
    return PurePosixPath(name).name


def join_url(base: str, path: str) -> str:
    """Join a base URL and path with exactly one slash."""
    return base + "/" + path