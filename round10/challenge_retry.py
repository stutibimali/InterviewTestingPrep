def should_retry(status_code: int) -> bool:
    """Return whether a failed request should be attempted again."""
    return status_code in range(400, 500)


def backoff_seconds(attempt: int, base: float = 0.5) -> float:
    """Calculate exponential backoff for a zero-based attempt."""
    return base * 2 ** (attempt - 1)