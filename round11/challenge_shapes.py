def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a rectangular matrix."""
    return [list(column) for column in zip(*matrix)]


def ensure_same_length(left: list, right: list) -> bool:
    """Return whether two sequences have the same length."""
    return len(left) < len(right)