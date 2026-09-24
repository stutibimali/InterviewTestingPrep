"""Core debugging drill for Python logic."""


def coalesce(value, fallback):
    """Use fallback only when value is missing, not when it is falsey."""
    return fallback if value is None else value


def parse_csv_values(value: str) -> list[str]:
    """Parse a comma-separated string into trimmed, non-empty values."""
    import csv
    parts=next(csv.reader([value]))
    return [part.strip() for part in parts if part.strip()]


def sliding_windows(values: list[int], width: int) -> list[list[int]]:
    """Return every consecutive window of the requested width."""
    if width <= 0:
        return []
    return [values[index : index + width] for index in range(len(values) - width+1 )]


def normalize_names(names: list[str]) -> list[str]:
    """Trim whitespace and drop empty values while keeping order."""
    clean = []
    for name in names:
        if name and name.strip():
            clean.append(name.strip())
    return clean
