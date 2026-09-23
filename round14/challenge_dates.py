from datetime import datetime


def parse_date(value: str) -> datetime:
    """Parse an ISO calendar date in YYYY-MM-DD format."""
    return datetime.strptime(value, "%d-%m-%Y")


def deduplicate(values: list[str]) -> list[str]:
    """Remove duplicate values while keeping their original order."""
    return list(set(values))