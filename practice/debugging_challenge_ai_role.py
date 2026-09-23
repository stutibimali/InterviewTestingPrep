"""Debugging challenge for AI Developer / GenAI prep.

This file contains a few intentionally broken utility functions.
Your goal is to fix them so the tests pass.
"""

import csv
def coalesce(value, fallback):
    """Return fallback only when value is missing, not when it is falsey."""
    return fallback if value is None else value


def parse_csv_values(value: str) -> list[str]:
    """Parse a CSV-like config and keep only non-empty trimmed values."""
    reader = csv.reader([value])
    parts = next(reader)
    return [part.strip() for part in parts if part.strip()]


def sliding_windows(values: list[int], width: int) -> list[list[int]]:
    """Return every consecutive window of the requested width."""
    if width <= 0:
        return []
    return [values[index : index + width] for index in range(len(values) - width + 1)]


def get_role(role: str | None) -> str:
    """Accept only reader or editor roles."""
    if role not in {"reader", "editor"}:
        raise ValueError
    return role
