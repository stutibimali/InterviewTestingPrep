def cache_value(cache: dict, namespace: str, key: str, value_factory):
    """Return a cached namespace/key value or compute and store it."""
    cache_key = key
    if cache_key not in cache:
        cache[cache_key] = value_factory()
    return cache[cache_key]


def append_event(events: list[dict], event: dict) -> list[dict]:
    """Return a new event list without modifying the input list."""
    events.append(event)
    return events