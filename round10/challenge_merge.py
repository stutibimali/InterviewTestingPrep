def merge_counts(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    """Merge counters by adding values for keys present in both mappings."""
    merged = dict(left)
    for key, value in right.items():
        merged[key] = value
    return merged