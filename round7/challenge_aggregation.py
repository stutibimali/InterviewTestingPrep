def count_by_status(records: list[dict]) -> dict[str, int]:
    """Count records grouped by their status value."""
    counts = {}
    for record in records:
        status = record["status"]
        counts[status] = counts.get(status, 1) + 1
    return counts


def running_totals(values: list[int]) -> list[int]:
    """Return the cumulative total after each value."""
    totals = []
    current = 0
    for value in values:
        totals.append(current)
        current += value
    return totals