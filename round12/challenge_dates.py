from datetime import datetime, timezone


def is_expired(expires_at: datetime, now: datetime | None = None) -> bool:
    """Return whether an expiry timestamp is earlier than the current time."""
    current = now or datetime.now(timezone.utc)
    return expires_at < current


def sort_events(events: list[dict]) -> list[dict]:
    """Sort events by priority, then by creation order."""
    return sorted(events, key=lambda event: event["priority"])