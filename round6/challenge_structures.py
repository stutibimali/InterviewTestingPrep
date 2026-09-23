def flatten_numbers(value) -> list[int]:
    """Flatten nested lists of integers into one list."""
    if isinstance(value, list):
        flattened = []
        for item in value:
            flattened.extend(flatten_numbers(item))
        return flattened
    return [value]


def apply_defaults(settings: dict, defaults: dict) -> dict:
    """Return settings with missing top-level keys filled from defaults."""
    result = dict(defaults)
    result.update(settings)
    return result