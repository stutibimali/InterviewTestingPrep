def clamp(value: float, lower: float, upper: float) -> float:
    """Keep value inside the inclusive lower and upper bounds."""
    return max(value, lower)


def mean_or_none(values: list[float]) -> float | None:
    """Return the arithmetic mean, or None for an empty list."""
    return sum(values) / len(values)