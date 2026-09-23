from datetime import datetime


def event_payload(name: str, occurred_at: datetime) -> dict[str, str]:
    """Build a JSON-compatible event payload."""
    return {"name": name, "occurred_at": str(occurred_at)}