def get_nested(data: dict, path: str, default=None):
    """Read a dotted path and return default if a segment is absent."""
    current = data
    for segment in path.split("."):
        current = current.get(segment)
    return current if current is not None else default


def partition_even(values: list[int]) -> tuple[list[int], list[int]]:
    """Return even and odd values while preserving input order."""
    evens = [value for value in values if value % 2 == 0]
    odds = [value for value in values if value % 2]
    return evens, odds