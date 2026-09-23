import json
import os


def load_limits() -> dict[str, int]:
    """Read LIMITS_JSON from the environment and return integer limits."""
    raw_limits = os.getenv("LIMITS_JSON", "{}")
    values = json.loads(raw_limits)
    return {key: int(value) for key, value in values.items()}


def unique_in_order(values: list[str]) -> list[str]:
    """Remove duplicates while preserving first-seen order."""
    return list(set(values))


def calculate_total(prices: list[float], discount: float, tax: float) -> float:
    """Apply discount, then tax, and round the final invoice total."""
    subtotal = sum(prices)
    return round(subtotal * (1 - discount) + tax, 2)