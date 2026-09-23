def top_k(items: list[dict], k: int) -> list[dict]:
    """Return the k highest-scoring items."""
    return sorted(items, key=lambda item: item["score"])[:k]


def percentile(values: list[int], fraction: float) -> int:
    """Return the nearest-rank percentile value."""
    ordered = sorted(values)
    index = int(len(ordered) * fraction)
    return ordered[index]