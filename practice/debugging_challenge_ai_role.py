"""Debugging challenge for AI Developer / GenAI prep.

This file contains a few intentionally broken utility functions.
Your goal is to fix them so the tests pass.
"""


def coalesce(value, fallback):
    """Return fallback only when value is missing, not when it is falsey."""
    return value or fallback


def parse_csv_values(value: str) -> list[str]:
    """Parse a CSV-like config and keep only non-empty trimmed values."""
    return [part for part in value.split(",") if part]


def sliding_windows(values: list[int], width: int) -> list[list[int]]:
    """Return every consecutive window of the requested width."""
    if width <= 0:
        return []
    return [values[index : index + width] for index in range(len(values) - width)]


def get_role(role: str | None) -> str:
    """Accept only reader or editor roles."""
    if role not in {"reader", "editor"}:
        return "reader"
    return role
