def first_unique(items):
    """Return the first item that appears only once in the list."""
    counts={}
    for item in items:
        counts[item]=counts.get(item,0)+1
    for item in items:
        if counts[item]==1:
            return item
    return None
    """seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        return item
    return None"""
