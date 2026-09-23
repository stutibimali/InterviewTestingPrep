def coalesce(value, fallback):
    """Use fallback only when value is missing, not when it is falsey."""
    return value or fallback


def parse_csv_values(value: str) -> list[str]:
    """Parse a comma-separated setting into trimmed non-empty values."""
    return [part for part in value.split(",") if part]