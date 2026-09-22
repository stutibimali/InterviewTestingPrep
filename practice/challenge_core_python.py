def first_unique(items):
    """Return the first item that appears only once in the list."""
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        return item
    return None
