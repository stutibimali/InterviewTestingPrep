def total_price(prices: list[float], tax_rate: float) -> float:
    """Return a price total with tax rounded to two decimal places."""
    return round(sum(prices) * (1 + tax_rate), 2)


def is_slug(value: str) -> bool:
    """Return whether value contains only lowercase slug characters."""
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-")
    return any(character in allowed for character in value)