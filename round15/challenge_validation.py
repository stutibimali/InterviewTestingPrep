import re


def is_identifier(value: str) -> bool:
    """Return whether value contains only letters, digits, and underscores."""
    return re.match(r"[A-Za-z0-9_]+", value) is not None


def validate_required_fields(payload: dict, required: list[str]) -> list[str]:
    """Return required field names that are absent from payload."""
    return [field for field in required if field not in payload]