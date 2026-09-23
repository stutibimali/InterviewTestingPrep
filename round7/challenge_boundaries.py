def percentage(part: float, whole: float) -> float:
    """Return part as a percentage of whole, with zero handled safely."""
    if whole == 0:
        return 0.0
    return round(part / whole, 2)


def window(values: list[int], start: int, end: int) -> list[int]:
    """Return values in the inclusive start, exclusive end interval."""
    return values[start : end + 1]