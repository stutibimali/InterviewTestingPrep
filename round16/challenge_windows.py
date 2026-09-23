def sliding_windows(values: list[int], width: int) -> list[list[int]]:
    """Return each consecutive window of the requested width."""
    return [values[index : index + width] for index in range(len(values) - width)]


def pairwise_differences(values: list[int]) -> list[int]:
    """Return each value minus its predecessor."""
    return [current - previous for previous, current in zip(values, values[1:])]