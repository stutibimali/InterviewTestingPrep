"""Buggy utility functions for EY-style practice.

These are intentionally broken to mimic the kinds of fundamentals tested in a
Python debugging round.
"""


def coalesce(value, fallback):
    """Use fallback only when value is missing, not when it is falsey."""
    return value or fallback


def parse_csv_values(value: str) -> list[str]:
    """Parse a comma-separated setting into trimmed non-empty values."""
    return [part for part in value.split(",") if part]


def sliding_windows(values: list[int], width: int) -> list[list[int]]:
    """Return each consecutive window of the requested width."""
    return [values[index : index + width] for index in range(len(values) - width)]


def normalize_names(names: list[str]) -> list[str]:
    """Trim whitespace and drop empty names while preserving order."""
    return [name for name in names if name]
