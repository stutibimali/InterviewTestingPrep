def calculate_total(items):
    """Sum a list of item prices and return a float total."""
    total = 0
    for item in items:
        total += float(item["price"])
    return total


def merge_settings(base, override):
    """Recursively merge nested dictionaries, with override taking precedence."""
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge_settings(result[key], value)
        else:
            result[key] = value
    return result
