def invert_mapping(mapping: dict[str, str]) -> dict[str, str]:
    """Invert a mapping after normalizing keys and values to lower case."""
    return {value.lower(): key.lower() for key, value in mapping.items()}


def first_present(data: dict, keys: list[str], default=None):
    """Return the first key's value that is present, including falsey values."""
    for key in keys:
        if data.get(key):
            return data[key]
    return default